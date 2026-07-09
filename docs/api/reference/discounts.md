# Discounts API Reference

## Overview

The Discounts application manages promotional pricing rules across the platform.

It provides coupon validation, discount calculation, and promotional campaigns while remaining independent from the order lifecycle.

---

# Responsibilities

The Discounts application manages:

- Coupons
- Promotional campaigns
- Percentage discounts
- Fixed amount discounts
- Validation rules
- Expiration dates
- Usage limits

---

# Base URL

```text
/api/v1/discounts/
```

---

# Main Resources

- Coupon
- Discount
- Promotion

---

# Available Endpoints

## Coupons

| Method | Endpoint | Authentication | Description |
|----------|----------------------------|---------------|-----------------------------|
| POST | /validate/ | JWT | Validate coupon |
| GET | /available/ | JWT | List available promotions |
| GET | /<code>/ | JWT | Coupon details |

---

# Coupon Validation

Validation includes:

- Coupon existence
- Active status
- Expiration date
- Usage limit
- User eligibility
- Minimum purchase amount

---

# Relationships

Discounts communicate with:

- Cart
- Orders

Discounts do not modify inventory or payments.

---

# Business Rules

A coupon:

- May expire.
- May have usage limits.
- May be user-specific.
- May require a minimum purchase amount.
- May be stackable or exclusive.

---

# Frontend Integration

Typical frontend usage:

- Coupon input during checkout.
- Promotion banners.
- Discount labels on products.
- Cart summary.

---

# Related Documentation

- Cart
- Orders
- Payments
