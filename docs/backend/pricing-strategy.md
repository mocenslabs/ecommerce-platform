# Pricing Strategy

## Price Composition

```text
Base Price

↓

Product Discount

↓

Coupon

↓

Taxes

↓

Shipping

↓

Final Total
```

---

## Discount Priority

Recommended evaluation order:

1. Product discount
2. Category discount
3. Coupon
4. Shipping promotion

---

## Rules

- Final price can never be negative.
- Coupons should be validated server-side.
- Discounts must be recalculated during checkout.
- Prices should never be trusted from the frontend.
