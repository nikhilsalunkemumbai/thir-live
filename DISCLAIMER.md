# Disclaimer

## Purpose

THIR (Threat Hunter Intelligence Range) is a **defensive security research project**.

This repository contains tools and infrastructure for operating a Cowrie SSH honeypot, collecting attacker telemetry, and visualising threat intelligence data. It is intended solely for:

- Threat research and intelligence gathering
- Security education and skill development
- Defensive monitoring of internet-facing infrastructure

## Honeypot Data

The dashboard at `threats.aegispub.com` displays **real attacker IPs and TTPs** captured by a live honeypot. This data is:

- Collected passively — the honeypot does not initiate contact
- Enriched using public APIs (AbuseIPDB, AlienVault OTX) under their respective terms of service
- Published for research and awareness purposes only

## No Offensive Use

The tools in this repository **must not** be used for:

- Unauthorised access to any system
- Active scanning or enumeration of third-party infrastructure
- Harassment, doxxing, or targeted action against any IP address or individual
- Any activity that violates local, national, or international law

## Third-Party Services

This project integrates with the following third-party APIs. Use of these services is subject to their own terms:

- [AbuseIPDB Terms of Service](https://www.abuseipdb.com/legal)
- [AlienVault OTX Terms of Service](https://otx.alienvault.com/api)
- [Cowrie Honeypot](https://github.com/cowrie/cowrie) — BSD 3-Clause License

## No Warranty

This software is provided "as is" without warranty of any kind. The authors are not responsible for any misuse, damage, or legal consequences arising from use of this project.

## Responsible Disclosure

If you believe any data published by this project causes harm or violates your rights, please open a GitHub issue or contact the repository owner directly.
