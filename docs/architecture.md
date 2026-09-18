# System Architecture & Technical Specifications

*Engineered by RJ Business Solutions for Davarus Bell Platform*

---

## 🏛️ SYSTEM OVERVIEW & TOPOLOGY

```
 [ Social Media / Media / Ad Traffic ]
                  │
                  ▼
    [ Cloudflare Anycast CDN & WAF ]
                  │
                  ▼
     [ Cloudflare Worker Edge Compute ]
      │ (Hono Framework / TypeScript)
      │
      ├───────────────────────┬───────────────────────┐
      │                       │                       │
      ▼                       ▼                       ▼
 [ Static Assets ]    [ API Engine ]          [ Edge Persistence ]
  - index.html         - POST /api/leads       - Cloudflare D1 (SQLite)
  - buy.html           - GET /api/leads          ├─ leads
  - sell.html          - GET /api/health         ├─ appointments
  - relocate.html                                └─ crm_activity_log
  - speaking.html
  - dev.html
```

---

## 💾 DATABASE ENTITY RELATIONSHIP (D1 SQLITE)

```
┌──────────────────────────────────────┐
│                LEADS                 │
├──────────────────────────────────────┤
│ id (PK)              TEXT            │
│ full_name            TEXT            │
│ email                TEXT            │
│ phone                TEXT            │
│ lead_type            TEXT            │
│ timeline             TEXT            │
│ budget_range         TEXT            │
│ loan_type            TEXT            │
│ preferred_cities     TEXT            │
│ created_at           TIMESTAMP       │
└──────────────────┬───────────────────┘
                   │ 1
                   │
                   │ N
┌──────────────────┴───────────────────┐
│           CRM_ACTIVITY_LOG           │
├──────────────────────────────────────┤
│ id (PK)              TEXT            │
│ lead_id (FK)         TEXT            │
│ action_type          TEXT            │
│ details              TEXT            │
│ timestamp            TIMESTAMP       │
└──────────────────────────────────────┘
```
