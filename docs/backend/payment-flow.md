# Payment Flow

## Standard Checkout Flow

```text
Customer

↓

Checkout

↓

Order Created

↓

Payment Created

↓

External Provider

↓

Provider Response

↓

Payment Updated

↓

Order Updated

↓

Notification Sent
```

---

## Failed Payment

```text
Payment Created

↓

Failed

↓

Order remains Pending

↓

Customer retries payment
```

---

## Successful Payment

```text
Pending

↓

Authorized

↓

Paid

↓

Order Confirmed

↓

Inventory Reserved / Updated
```

---

## Future Extensions

- Refunds
- Chargebacks
- Partial Payments
- Multiple Payment Attempts
- Split Payments
