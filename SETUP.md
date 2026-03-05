# THIR Setup Guide

Complete setup instructions for deploying THIR from scratch.

## Prerequisites

- AWS account (free tier sufficient)
- GitHub account
- Cloudflare account (free tier) with your domain configured
- AbuseIPDB account (free) — [abuseipdb.com](https://www.abuseipdb.com)
- AlienVault OTX account (free) — [otx.alienvault.com](https://otx.alienvault.com)

---

## Step 1 — AWS EC2 Instance

1. EC2 → Launch Instance
2. **AMI:** Ubuntu Server 22.04 LTS
3. **Type:** t2.micro (free tier)
4. **Key pair:** Create new → download `.pem` file
5. **Security group inbound rules:**
   - TCP 22 → Your IP only (admin SSH)
   - TCP 2222 → 0.0.0.0/0 (Cowrie honeypot, public)

---

## Step 2 — Install Cowrie on EC2

```bash
# Connect
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>

# Install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv \
  python3-dev libssl-dev libffi-dev build-essential authbind

# Create cowrie user
sudo adduser --disabled-password cowrie
sudo su - cowrie

# Clone and install
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

# Create start script
cat > bin/cowrie << 'EOF'
#!/bin/bash
COWRIE_HOME=$(dirname $(dirname $(readlink -f $0)))
cd $COWRIE_HOME
source cowrie-env/bin/activate
case "$1" in
  start)   twistd --pidfile var/run/cowrie.pid --logfile var/log/cowrie/cowrie.log cowrie ;;
  stop)    kill $(cat var/run/cowrie.pid) ;;
  status)  [ -f var/run/cowrie.pid ] && kill -0 $(cat var/run/cowrie.pid) 2>/dev/null \
             && echo "cowrie is running" || echo "cowrie is NOT running" ;;
  restart) $0 stop && sleep 2 && $0 start ;;
esac
EOF
chmod +x bin/cowrie

# Start
bin/cowrie start
bin/cowrie status
exit  # back to ubuntu user
```

---

## Step 3 — GitHub Deploy Key

```bash
# As ubuntu user on EC2
ssh-keygen -t ed25519 -C "thir-pipeline" -f ~/.ssh/thir_deploy -N ""

# Create cowrie .ssh dir and add key
sudo mkdir -p /home/cowrie/.ssh
sudo touch /home/cowrie/.ssh/authorized_keys
sudo chmod 700 /home/cowrie/.ssh
sudo chmod 600 /home/cowrie/.ssh/authorized_keys
sudo chown -R cowrie:cowrie /home/cowrie/.ssh
sudo bash -c 'cat /home/ubuntu/.ssh/thir_deploy.pub >> /home/cowrie/.ssh/authorized_keys'

# Print private key — copy for GitHub secret
cat ~/.ssh/thir_deploy

# Print EC2 public IP — copy for GitHub secret
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

| Secret Name | Value |
|---|---|
| `ORACLE_VPS_SSH_KEY` | Private key from Step 3 (entire contents including headers) |
| `ORACLE_VPS_IP` | EC2 public IP from Step 3 |
| `ABUSEIPDB_API_KEY` | From abuseipdb.com → Account → API |
| `OTX_API_KEY` | From otx.alienvault.com → top-right avatar → API Key |

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

Watch the logs. All 13 steps should pass. After ~2 minutes, `data/*.json` files will appear in the repo and the dashboard will go live.

---

## Verification Checklist

```
✅ Cowrie running: bin/cowrie status
✅ Logs writing: tail -f ~/cowrie/var/log/cowrie/cowrie.json
✅ Port 2222 open: nc -zv <EC2_IP> 2222
✅ GitHub Actions run succeeded
✅ data/*.json files in repo
✅ threats.aegispub.com loads dashboard
✅ Dashboard shows MONITORING (not OFFLINE)
```
