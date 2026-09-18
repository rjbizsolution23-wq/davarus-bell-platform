# ADR 0002: Cloudflare D1 SQLite for Edge CRM Persistence

## Status
Accepted

## Context
Lead captures from homebuyer qualification quizzes, seller net sheets, and speaking booking forms need persistent structured storage that is accessible globally at the edge without expensive third-party database latency.

## Decision
We choose **Cloudflare D1 (Serverless SQLite at the Edge)**.

## Consequences
* **Positives:**
  * Zero-latency SQL queries co-located with Cloudflare Worker compute.
  * Direct support for transactional lead tracking and activity logging.
  * Cost-effective serverless pricing scale.
* **Negatives:**
  * SQLite concurrency limits for massive batch writes (mitigated by asynchronous Queues if traffic spikes).
