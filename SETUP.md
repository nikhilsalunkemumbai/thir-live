# THIR Setup Guide

Complete setup instructions for deploying THIR from scratch.

## Prerequisites

- AWS account (free tier sufficient)
- GitHub account
- Cloudflare account (free tier) with your domain configured
- AbuseIPDB account (free) — [abuseipdb.com](https://www.abuseipdb.com)
- AlienVault OTX account (free) — [otx.alienvault.com](https://otx.alienvault.com)

> **Port note:** Port 22 on the EC2 instance is redirected to Cowrie via iptables so attackers land in the honeypot. All pipeline SSH/SCP access uses **port 22222** (the real management port). Never use port 22 for admin or pipeline access.

---

## Step 1 — AWS EC2 Instance

1. EC2 → Launch Instance
2. **AMI:** Ubuntu Server 22.04 LTS
3. **Type:** t2.micro (free tier)
4. **Key pair:** Create new → download `.pem` file
5. **Security group inbound rules:**
   - TCP 22222 → Your IP only (admin SSH — real management port)
   - TCP 2222 → 0.0.0.0/0 (Cowrie honeypot, public)
   - TCP 22 → 0.0.0.0/0 (redirect to Cowrie via iptables — see Step 2d)

---

## Step 2 — Install Cowrie on EC2

### 2a. Connect and install dependencies

```bash
ssh -i your-key.pem -p 22222 ubuntu@<EC2_PUBLIC_IP>

sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv \
  python3-dev libssl-dev libffi-dev build-essential authbind
```

### 2b. Create cowrie user and install Cowrie

```bash
sudo adduser --disabled-password cowrie
sudo su - cowrie

git clone https://github.com/cowrie/cowrie.git
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Configure
cp etc/cowrie.cfg.dist etc/cowrie.cfg
# Edit etc/cowrie.cfg:
#   hostname = web-server-01
#   listen_port = 2222
#   [output_jsonlog] enabled = true

# Start
bin/cowrie start
bin/cowrie status
exit  # back to ubuntu user
```

### 2c. Move real SSH to port 22222

```bash
sudo sed -i 's/#Port 22/Port 22222/' /etc/ssh/sshd_config
sudo systemctl restart sshd
# Verify new port works before proceeding:
# ssh -i your-key.pem -p 22222 ubuntu@<EC2_IP>
```

### 2d. Redirect port 22 to Cowrie

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo apt install -y iptables-persistent
sudo netfilter-persistent save
```

---

## Step 3 — GitHub Deploy Key

```bash
# As ubuntu user on EC2 (port 22222)
ssh-keygen -t ed25519 -C "thir-pipeline" -f ~/.ssh/thir_deploy -N ""

# Add public key to cowrie user's authorized_keys
sudo mkdir -p /home/cowrie/.ssh
sudo touch /home/cowrie/.ssh/authorized_keys
sudo chmod 700 /home/cowrie/.ssh
sudo chmod 600 /home/cowrie/.ssh/authorized_keys
sudo chown -R cowrie:cowrie /home/cowrie/.ssh
sudo bash -c 'cat /home/ubuntu/.ssh/thir_deploy.pub >> /home/cowrie/.ssh/authorized_keys'

# Print private key — copy for GitHub secret ORACLE_VPS_SSH_KEY
cat ~/.ssh/thir_deploy

# Print EC2 public IP — copy for GitHub secret ORACLE_VPS_IP
curl -s https://checkip.amazonaws.com
```

---

## Step 4 — GitHub Repository

1. Create new repo: `thir-live` (public, no README)
2. Push this codebase:
   ```bash
   git init
   git add .
   git commit -m "init: THIR live pipeline"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/thir-live.git
   git push -u origin main
   ```

---

## Step 5 — GitHub Secrets

Repo → Settings → Secrets and variables → Actions → New repository secret

**Required:**

| Secret Name | Value |
|---|---|
| `ORACLE_VPS_SSH_KEY` | Private key from Step 3 (entire contents including headers) |
| `ORACLE_VPS_IP` | EC2 public IP from Step 3 |
| `ABUSEIPDB_API_KEY` | From abuseipdb.com → Account → API |
| `OTX_API_KEY` | From otx.alienvault.com → top-right avatar → API Key |

**Optional:**

| Secret Name | Value |
|---|---|
| `VIRUSTOTAL_API_KEY` | From virustotal.com — enables Tool 31 hash lookups (free tier safe) |
| `ALERT_CHANNEL` | `slack` \| `email` \| `both` \| `dry-run` (default: `dry-run`) |
| `SLACK_WEBHOOK_URL` | Slack incoming webhook — required if `ALERT_CHANNEL` includes `slack` |
| `SMTP_HOST` | SMTP server hostname — required if `ALERT_CHANNEL` includes `email` |
| `SMTP_PORT` | SMTP port (e.g. `587`) |
| `SMTP_USER` | SMTP username |
| `SMTP_PASS` | SMTP password |
| `ALERT_EMAIL_FROM` | Sender address for email alerts |
| `ALERT_EMAIL_TO` | Recipient address for email alerts |

---

## Step 6 — GitHub Pages

Repo → Settings → Pages → Source: **Deploy from branch** → Branch: `main` / `/ (root)` → Save

---

## Step 7 — Cloudflare DNS

Cloudflare → your domain → DNS → Add record:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | threats | YOUR_USERNAME.github.io | ✅ Proxied |

---

## Step 8 — Integrity Baseline (run once)

```bash
# Clone repo locally, then:
go run tools/07_file_integrity_live.go \
  --create-baseline data/integrity_baseline.json \
  --path data/
git add data/integrity_baseline.json
git commit -m "init: integrity baseline"
git push
```

---

## Step 9 — First Pipeline Run

GitHub → Actions → **THIR Live Pipeline** → Run workflow

Watch the logs. All steps should pass. After ~2–3 minutes, `data/*.json` files will appear in the repo and the dashboard will go live.

---

## Verification Checklist

```
✅ Real SSH on port 22222: ssh -i your-key.pem -p 22222 ubuntu@<EC2_IP>
✅ Port 22 goes to Cowrie: ssh ubuntu@<EC2_IP>  (should land in honeypot)
✅ Cowrie running: bin/cowrie status
✅ Logs writing: tail -f ~/cowrie/var/log/cowrie/cowrie.json
✅ Port 2222 open: nc -zv <EC2_IP> 2222
✅ GitHub Actions run succeeded
✅ data/*.json files in repo
✅ threats.aegispub.com loads dashboard
✅ Dashboard shows MONITORING (not OFFLINE)
```

---

## Troubleshooting

**Pipeline fails at SCP step with "Connection refused"**
- Verify the EC2 IP in `ORACLE_VPS_IP` secret is current (Elastic IP recommended)
- Confirm port 22222 is open in the EC2 security group for the GitHub Actions IP range
- Check `continue-on-error: true` on the pre-flight step — the pipeline continues even if the honeypot is temporarily unreachable

**Pipeline ran but `data/*.json` shows no new cases**
- Check the watermark: `data/cowrie_watermark.json` shows the last processed line count
- If Cowrie was rotated, delete `cowrie_watermark.json` and re-run — the pipeline will do a full fetch
- Confirm Cowrie is running: `bin/cowrie status` on the EC2

**Dashboard shows OFFLINE**
- Tool 05 checks port 2222 on the honeypot EC2. OFFLINE means the Cowrie process has stopped — restart it: `bin/cowrie start`

**Tool 31 / Tool 33 never run**
- These tools only run when `ir_cases.json` contains sessions with `downloads`. If attackers have not downloaded any files, these tools are skipped — this is expected behavior.

**Alert emails/Slack not firing**
- Confirm `ALERT_CHANNEL` secret is set (default is `dry-run` — no external alerts sent)
- For Slack: verify `SLACK_WEBHOOK_URL` is set and the webhook is active
- Check `data/alert_history.json` — if an alert was already fired for the same finding, it will be deduplicated
