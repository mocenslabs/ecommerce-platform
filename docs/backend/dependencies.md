# Backend Dependency Map

```text
Core
│
├── Authentication
│     └── Users
│
├── Catalog
│     ├── Inventory
│     ├── Reviews
│     └── Wishlist
│
├── Cart
│
├── Orders
│
├── Payments
│
├── Discounts
│
├── Notifications
│
├── Dashboard
│
└── Audit
```

## Dependency Rules

Core must never depend on business applications.

Catalog owns product information.

Inventory owns stock.

Cart owns temporary purchases.

Orders own business transactions.

Payments own financial transactions.

Audit records events only.

Dashboard aggregates data only.
