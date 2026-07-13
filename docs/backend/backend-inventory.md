# Backend Inventory

## Overview

The backend is organized as a modular Django project following a domain-driven approach.

Applications:

| Application | Purpose | Status |
|------------|---------|--------|
| core | Shared infrastructure and utilities | Reviewed |
| authentication | Authentication and JWT management | Pending |
| users | User management | Pending |
| catalog | Product catalog | Pending |
| inventory | Inventory management | Pending |
| cart | Shopping cart | Pending |
| wishlist | Wishlist management | Pending |
| orders | Order lifecycle | Pending |
| payments | Payment processing | Pending |
| discounts | Discounts and coupons | Pending |
| reviews | Product reviews | Pending |
| notifications | Notifications | Pending |
| dashboard | Administrative dashboard | Pending |
| audit | Audit logs | Pending |

---

# Dependency Order

Core

↓

Authentication

↓

Users

↓

Catalog

↓

Inventory

↓

Cart

↓

Wishlist

↓

Orders

↓

Payments

↓

Discounts

↓

Reviews

↓

Notifications

↓

Dashboard

↓

Audit

---

# Review Progress

| Module            | Architecture | API | Audit | Documentation |
|-------------------|--------------|-----|-------|---------------|
| Core              |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Authentication    |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Users             |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Catalog           |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Inventory         |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Cart              |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Wishlist          |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Orders            |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Payments          |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Discounts         |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Reviews           |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Notifications     |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Dashboard         |     ⏳       | ⏳  |   ⏳  |      ⏳       |
| Audit             |     ⏳       | ⏳  |   ⏳  |      ⏳       |

---

# Documentation Goals

For every application the following documents will be produced:

- API Reference
- Technical Audit
- Business Rules
- Frontend Integration Notes

---

# Completion Criteria

A module is considered complete when:

- Architecture reviewed.
- Models documented.
- Services documented.
- Serializers documented.
- Views documented.
- URLs documented.
- Permissions documented.
- API examples written.
- Audit completed.
