# System Overview

## High-Level Architecture

```text
               Vue Frontend
                     │
                     ▼
              Django REST API
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 PostgreSQL        Redis         Celery
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              External Services

            Payment Providers
            Email Provider
            Cloud Storage
```

---

## Main Components

- Frontend
- Backend API
- Database
- Cache
- Background Workers
- Storage
- External Integrations
