# State Machines

## Order Lifecycle

```text
Pending
    │
    ▼
Confirmed
    │
    ▼
Paid
    │
    ▼
Processing
    │
    ▼
Shipped
    │
    ▼
Delivered
```

Cancellation may occur before shipment.

```text
Pending
    │
    └──────────────► Cancelled

Confirmed
    │
    └──────────────► Cancelled
```

Paid orders may require a refund workflow rather than direct cancellation.

---

## Business Rules

Allowed transitions only.

Invalid transitions must be rejected by the backend.

Examples:

❌ Delivered → Pending

❌ Cancelled → Paid

❌ Delivered → Processing
