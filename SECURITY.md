# Security Policy

## Supported Versions

This project is actively maintained. Security fixes are applied to the `main` branch only.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub Issues.**

If you discover a security issue in this project — including vulnerabilities in the pipeline tools, dashboard, or honeypot configuration — please report it privately by:

1. Opening a **GitHub Security Advisory** (Repository → Security → Advisories → New draft)
2. Or contacting the repository owner directly via GitHub

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We aim to respond within **72 hours** and will keep you informed as the issue is addressed.

## Scope

| In Scope | Out of Scope |
|---|---|
| Pipeline tool vulnerabilities (tools/) | Third-party APIs (AbuseIPDB, OTX) |
| Data injection via crafted Cowrie logs | Cowrie honeypot itself |
| Dashboard XSS or data exposure | GitHub Actions runner infrastructure |
| SSH key or secret exposure | AWS EC2 configuration |

## Known Design Decisions

- Honeypot data (attacker IPs, commands) is published publicly via GitHub Pages. This is intentional — it is sanitised via `sanitise_ip()` and `sanitise_session_id()` before publication.
- The pipeline runs with `contents: write` permission scoped to the repo only.
- SSH keys for EC2 access are stored as GitHub Actions secrets and deleted from the runner after each run.
