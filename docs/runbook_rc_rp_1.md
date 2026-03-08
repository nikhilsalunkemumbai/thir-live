# THIR Recovery Runbook
## RC.RP-1 — Recovery Planning
### If the AWS EC2 Honeypot Is Compromised or Lost

---

**Document ID:** THIR-RC-RP-1  
**NIST CSF Control:** RC.RP-1 — Recovery plan is executed during or after a cybersecurity incident  
**NIST Function:** RECOVER  
**Asset Covered:** AWS EC2 Ubuntu — Cowrie SSH Honeypot (`thir-honeypot-01`)  
**Owner:** Joy Dane  
**Last Reviewed:** 2025-03-08  

---

## 1. Purpose

This runbook documents the step-by-step procedure to recover the THIR honeypot infrastructure if the AWS EC2 instance is compromised, corrupted, terminated, or otherwise unavailable. It exists so recovery can begin immediately without making decisions under pressure.

A honeypot getting compromised is not a failure. It is the expected outcome of intentional exposure. The goal is to restore the sensor quickly, cleanly, and from a known-good state.

---

## 2. Recovery Trigger Conditions

Execute this runbook if any of the following are true:

| Condition | How You Know |
|---|---|
| EC2 instance unreachable | Tool 05 reports `DOWN` in `data/posture.json` for 2+ consecutive hourly runs |
| Pipeline SCP step fails | GitHub Actions log shows `Permission denied` or `Connection refused` on the fetch step |
| Cowrie log file missing or empty | Pre-flight step reports `No such file or directory` for `cowrie.json` |
| EC2 instance terminated | AWS console shows instance state as `terminated` |
| Attacker achieved root on the EC2 host (not inside Cowrie) | `cowrie.json` contains events showing `/proc`, `/etc/shadow`, or `iptables` commands that Cowrie would not normally emulate |
| Unexpected outbound traffic from EC2 IP | AbuseIPDB reports your own VPS IP as a threat actor |

---

## 3. Do Not Do This First

Before taking any action, **preserve evidence**:

- Take an AWS snapshot of the EBS volume before terminating or rebuilding
- Download the current `cowrie.json` and any rotated logs (`cowrie.json.YYYY-MM-DD`) to a local machine
- Note the exact time you discovered the issue — this is T0 for your incident timeline

Evidence first. Rebuild second. This is a security project. The compromise is the data.

---

## 4. Recovery Procedure

### Phase 1 — Isolate (5 minutes)

```bash
# Step 1: Detach the EC2 instance from the internet
# AWS Console → EC2 → Security Groups → remove inbound rule for port 2222
# This stops further attacker access without destroying evidence

# Step 2: Revoke the GitHub Actions SSH key on the EC2 side
# SSH in (if still possible) and remove from authorized_keys
nano /home/ubuntu/.ssh/authorized_keys
# Delete the github-actions line, save

# Step 3: Rotate the GitHub Secret
# GitHub → repo Settings → Secrets → ORACLE_VPS_SSH_KEY
# Generate new key pair, update secret — pipeline will fail safely until rebuilt
```

---

### Phase 2 — Preserve Evidence (10 minutes)

```bash
# From your local machine, SCP all logs before any rebuild
scp -i ~/.ssh/your_key ubuntu@YOUR_EC2_IP:/home/cowrie/cowrie/var/log/cowrie/* ./evidence/

# Also grab auth.log and syslog from the host OS itself
scp -i ~/.ssh/your_key ubuntu@YOUR_EC2_IP:/var/log/auth.log ./evidence/
scp -i ~/.ssh/your_key ubuntu@YOUR_EC2_IP:/var/log/syslog ./evidence/

# Take AWS EBS snapshot
# AWS Console → EC2 → Volumes → select root volume → Actions → Create Snapshot
# Label it: thir-compromise-evidence-YYYY-MM-DD
```

---

### Phase 3 — Rebuild EC2 (20 minutes)

```bash
# Option A: New instance from scratch (cleanest)
# 1. Launch new EC2: Ubuntu 22.04 LTS, t2.micro (free tier), same region
# 2. Create new key pair, download .pem
# 3. Security Group: allow SSH port 22 (your IP only), port 2222 (0.0.0.0/0 for honeypot)
# 4. Elastic IP: allocate a new one and associate it
# 5. Update GitHub Secret ORACLE_VPS_IP with the new Elastic IP

# Option B: Reimage existing instance
# AWS Console → EC2 → stop instance → detach EBS → attach fresh Ubuntu AMI volume

# Install Cowrie on the new instance:
ssh -i ~/.ssh/new_key ubuntu@NEW_EC2_IP

sudo apt update && sudo apt install -y python3-virtualenv git libssl-dev libffi-dev \
  build-essential libpython3-dev python3-minimal authbind virtualenv

sudo adduser --disabled-password cowrie
sudo su - cowrie

git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cp etc/cowrie.cfg.dist etc/cowrie.cfg

# Configure cowrie.cfg
nano etc/cowrie.cfg
# Set: [ssh] listen_port = 2222
# Set: [output_jsonlog] enabled = true

# Start Cowrie
bin/cowrie start

# Verify log file is being created
ls -lh var/log/cowrie/
```

---

### Phase 4 — Restore Pipeline Access (5 minutes)

```bash
# Generate new SSH key for GitHub Actions
ssh-keygen -t ed25519 -C "thir-pipeline" -f ~/.ssh/thir_actions_key -N ""

# Add public key to new EC2
ssh-copy-id -i ~/.ssh/thir_actions_key.pub ubuntu@NEW_EC2_IP

# Update GitHub Secrets
# ORACLE_VPS_SSH_KEY  → contents of thir_actions_key (private key, full PEM)
# ORACLE_VPS_IP       → new EC2 Elastic IP (if changed)

# Trigger pipeline manually to verify
# GitHub → Actions → THIR Live Pipeline → Run workflow
```

---

### Phase 5 — Verify Recovery (5 minutes)

Confirm all of the following before closing this runbook:

- [ ] Tool 05 reports `UP` in `data/posture.json`
- [ ] GitHub Actions pipeline runs to completion without errors
- [ ] `data/ir_cases.json` is being updated with new sessions
- [ ] `threats.aegispub.com` dashboard shows live data
- [ ] Old EC2 instance terminated (or snapshot retained and instance stopped)
- [ ] Evidence files stored locally
- [ ] Incident documented as an IR case in the THIR dashboard

---

## 5. Recovery Time Objectives

| Target | Time |
|---|---|
| Evidence preserved | Within 15 minutes of detection |
| New EC2 running with Cowrie | Within 45 minutes of decision to rebuild |
| Pipeline restored and verified | Within 60 minutes of decision to rebuild |
| **Total RTO (Recovery Time Objective)** | **< 90 minutes** |

---

## 6. Seed Data for `data/assets.json`

After rebuild, Tool 05 will regenerate `assets.json` automatically on the next pipeline run. No manual intervention needed — the `--assets data/assets.json` flag handles it. `first_seen` will reset to the new build date, which is accurate.

---

## 7. Post-Recovery Actions

1. Write an IR case for the compromise event — add it to the THIR dashboard
2. Review Cowrie logs from the evidence folder — what did the attacker do?
3. Check if any TTPs from the compromise map to new MITRE techniques not yet in the heatmap
4. If root was achieved: review whether Cowrie's `fake_` filesystem emulation needs hardening
5. Update this runbook with any steps that were missing or unclear

---

## 8. NIST CSF Alignment

| Control | How This Runbook Covers It |
|---|---|
| **RC.RP-1** | This document IS the recovery plan. It is written, versioned, and tested. |
| **RS.RP-1** | Phase 1 isolation procedure maps to the IR containment plan |
| **RS.AN-1** | Phase 2 evidence preservation supports the investigation process |
| **PR.IP-4** | Backups (EBS snapshot) are taken before rebuild |
| **ID.AM-1** | Asset is re-registered in `assets.json` after rebuild via Tool 05 |

---

*This runbook is version-controlled in the THIR repository. Any changes to the EC2 configuration, Cowrie setup, or pipeline secrets should be reflected here before the change is made — not after.*
