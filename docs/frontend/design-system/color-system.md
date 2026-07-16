# Color System

## Document Information

| Field         | Value                       |
|---------------|-----------------------------|
| Document Name | Color System                |
| Version       | 1.0                         |
| Status        | Active                      |
| Area          | Frontend Engineering        |
| Scope         | Premium E-commerce Platform |
| Last Updated  | 2026-07-14                  |

---

# 1. Purpose

This document defines the color strategy used by the frontend Design System.

The objective is to create a consistent, accessible, and professional visual language.

Colors should communicate meaning and guide user interaction.

---

# 2. Color Philosophy

Color should be used intentionally.

The interface should not depend on excessive use of brand colors.

The design approach follows:

- neutral foundations;
- strategic accent usage;
- clear visual hierarchy;
- meaningful states.

---

# 3. Color Categories

The system is divided into:

```text
Brand Colors

↓

Semantic Colors

↓

Neutral Colors

↓

Interaction States
```

---

# 4. Brand Colors

Brand colors represent the visual identity of the product.

They should be used for:

- primary actions;
- important highlights;
- brand recognition.

Examples:

```css
--color-primary;

--color-secondary;

--color-accent;
```

Brand colors should not dominate every interface element.

---

# 5. Primary Color

The primary color represents the main action color.

Used for:

- primary buttons;
- important links;
- highlighted actions;
- selected states.

Example:

```css
--color-primary;
--color-primary-hover;
--color-primary-active;
```

---

# 6. Secondary Color

The secondary color supports the primary identity.

Used for:

- complementary actions;
- visual balance;
- secondary emphasis.

Example:

```css
--color-secondary;
```

---

# 7. Accent Color

Accent colors create visual interest.

Used carefully for:

- promotions;
- important information;
- special highlights.

Accent colors should improve attention, not create visual noise.

---

# 8. Semantic Colors

Semantic colors communicate system states.

## Success

Used for:

- completed actions;
- confirmations;
- positive feedback.

```css
--color-success;
```

---

## Warning

Used for:

- attention required;
- possible issues.

```css
--color-warning;
```

---

## Error

Used for:

- failures;
- invalid actions;
- destructive states.

```css
--color-error;
```

---

## Info

Used for:

- informative messages;
- neutral notifications.

```css
--color-info;
```

---

# 9. Neutral Color Scale

Neutral colors provide the structural foundation.

Used for:

- backgrounds;
- surfaces;
- text;
- borders;
- separators.

Examples:

```css
--color-background;

--color-surface;

--color-surface-elevated;

--color-text-primary;

--color-text-secondary;

--color-border;
```

---

# 10. Light and Dark Theme Strategy

The application supports theme-based color adaptation.

Themes should modify semantic tokens.

Example:

```text
Light Theme

↓

Semantic Tokens

↓

Components
```

and:

```text
Dark Theme

↓

Same Semantic Tokens

↓

Different Values
```

Components should not know which theme is active.

---

# 11. Ecommerce Specific Usage

Colors should support ecommerce experiences.

Examples:

## Product Availability

```text
Available
Low Stock
Unavailable
```

## Purchase Flow

```text
Added to Cart
Payment Approved
Payment Failed
```

## Promotions

```text
Discount
Featured Product
Special Offer
```

---

# 12. Color Usage Rules

Developers should:

- use semantic tokens;
- maintain contrast;
- avoid random colors;
- reuse existing definitions.

Avoid:

```css
color: #ff0000;
```

Prefer:

```css
color: var(--color-error);
```

---

# 13. Accessibility Requirements

Colors must consider:

- contrast ratios;
- readable text;
- non-color indicators;
- different visual abilities.

Color alone should not communicate critical information.

---

# 14. Visual Direction

The ecommerce interface should communicate:

- trust;
- simplicity;
- modernity;
- professionalism.

The design should avoid:

- excessive saturation;
- visual overload;
- unnecessary gradients;
- inconsistent colors.

---

# 15. Future Evolution

The color system may evolve as the product grows.

Changes should:

- improve usability;
- maintain consistency;
- preserve accessibility.

---

# Related Documents

- Design System Overview
- Design Tokens
- Typography
- Accessibility
- Component Library

---

# Document Status

Status: Active

Version: 1.0
