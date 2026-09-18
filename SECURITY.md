# Security Policy

## Supported Versions

| Version | Supported | Notes |
| :--- | :--- | :--- |
| 1.x.x | Yes | Active Production Version |

## Reporting a Vulnerability

**Do NOT open a public GitHub issue for security vulnerabilities.**

If you discover a security vulnerability or exposed key, please notify the security team directly:

* **Security Email:** `support@rjbusinesssolutions.org`
* **Lead Architect:** Rick Jefferson (CEO, RJ Business Solutions)
* **Response SLA:** Within 24 hours

## Security Controls Implemented

* Zero secrets committed to source control (`.env` ignored).
* Input sanitization & validation on all `/api/leads` HTTP POST payloads.
* Cloudflare WAF & rate-limiting protection.
* Strict TCPA-compliant lead consent capture.
