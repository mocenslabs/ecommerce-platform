# Business Rules

## Authentication

- Users must authenticate using JWT.
- Email verification is required if enabled.
- Password reset tokens expire.

---

## Catalog

- Only active products are publicly visible.
- Products require a category.
- Slugs must be unique.

---

## Inventory

- Stock cannot become negative.
- Availability depends on active stock.

---

## Cart

- Only authenticated users own carts.
- Quantities must be validated.
- Cart totals are calculated server-side.

---

## Discounts

- Coupons expire.
- Coupons are validated server-side.
- Discounts cannot generate negative totals.

---

## Orders

- Orders require a valid cart.
- Orders are immutable after confirmation.
- Order totals are calculated on the backend.

---

## Payments

- Payments belong to orders.
- Client-side payment confirmation is never trusted.
- Webhooks are authoritative.

---

## Reviews

- Reviews belong to one user.
- Reviews belong to one product.

---

## Notifications

- Notifications are event-driven.

---

## Audit

- Audit events are immutable.
