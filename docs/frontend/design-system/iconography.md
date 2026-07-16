# Iconography System

## Document Information

| Field | Value |
|---|---|
| Document Name | Iconography System |
| Version | 1.0 |
| Status | Active |
| Area | Frontend Engineering |
| Scope | Premium E-commerce Platform |
| Last Updated | 2026-07-14 |

---

# 1. Purpose

This document defines the iconography standards used by the frontend Design System.

The goal is to provide a consistent visual language for actions, navigation, information, and system states.

---

# 2. Icon Philosophy

Icons should improve understanding.

They should:

- support user recognition;
- simplify interactions;
- reinforce meaning.

Icons should not replace clear communication when the meaning is ambiguous.

---

# 3. Icon Library

The application uses a centralized icon library.

The selected icon system must provide:

- consistent style;
- accessibility support;
- scalable vectors;
- active maintenance.

---

# 4. Icon Style

All icons should follow the same visual characteristics.

Requirements:

- consistent stroke weight;
- consistent proportions;
- similar visual density;
- predictable rendering.

Avoid mixing multiple icon styles.

---

# 5. Icon Categories

Icons are grouped by purpose.

## Navigation Icons

Examples:

```text
Home

Search

Menu

Arrow
```

---

## Commerce Icons

Examples:

```text
Cart

Wishlist

Product

Discount

Payment
```

---

## User Icons

Examples:

```text
Account

Profile

Settings

Security
```

---

## System Icons

Examples:

```text
Success

Warning

Error

Information
```

---

# 6. Icon Sizes

Icons use predefined sizes.

Example:

```text
Small

16px


Medium

20px


Large

24px


Extra Large

32px+
```

---

# 7. Icon Tokens

Icon sizes should be centralized.

Example:

```css
--icon-sm;

--icon-md;

--icon-lg;

--icon-xl;
```

---

# 8. Icon Colors

Icons should use semantic colors.

Example:

```css
color: var(--color-text-secondary);
```

or:

```css
color: var(--color-primary);
```

Avoid:

```css
color: #333333;
```

---

# 9. Interactive Icons

Clickable icons must provide feedback.

Examples:

- hover state;
- focus state;
- active state.

Example:

```text
Default

↓

Hover

↓

Active
```

---

# 10. Accessibility

Icons must consider:

- meaningful labels;
- keyboard accessibility;
- screen readers.

Decorative icons should be hidden from assistive technologies.

Example:

```text
Decorative icon

aria-hidden="true"
```

---

# 11. Ecommerce Usage

Icons support important shopping experiences.

Examples:

## Product Discovery

- search;
- filters;
- categories.

## Shopping Flow

- cart;
- checkout;
- payment.

## Customer Area

- orders;
- notifications;
- profile.

---

# 12. Icon Component

Icons should be wrapped in a reusable component.

Example:

```text
components/

base/

Icon.vue
```

Responsibilities:

- size control;
- color handling;
- accessibility attributes;
- consistent rendering.

---

# 13. Implementation Rules

Developers should:

- use approved icons;
- reuse existing icons;
- maintain consistency.

Avoid:

- random SVG files;
- inline duplicated icons;
- mixing libraries.

---

# 14. Benefits

This iconography system provides:

- consistent interface language;
- easier maintenance;
- improved usability;
- professional appearance.

---

# Related Documents

- Design System Overview
- Design Tokens
- Component Library
- Accessibility
- Motion System

---

# Document Status

Status: Active

Version: 1.0
