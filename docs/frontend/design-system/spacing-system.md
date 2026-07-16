# Spacing System

## Document Information

| Field | Value |
|---|---|
| Document Name | Spacing System |
| Version | 1.0 |
| Status | Active |
| Area | Frontend Engineering |
| Scope | Premium E-commerce Platform |
| Last Updated | 2026-07-14 |

---

# 1. Purpose

This document defines the spacing strategy used by the frontend Design System.

The spacing system establishes consistent relationships between interface elements.

Its purpose is to provide:

- visual rhythm;
- alignment;
- consistency;
- maintainability.

---

# 2. Spacing Philosophy

Spacing is a design decision.

Every distance between elements should have a clear purpose.

The application should avoid arbitrary spacing values.

Incorrect:

```css
margin: 17px;
```

Correct:

```css
margin: var(--spacing-md);
```

---

# 3. Spacing Scale

The system uses a predefined spacing scale.

Example:

```text
4px

8px

12px

16px

24px

32px

48px

64px

96px
```

---

# 4. Spacing Tokens

Spacing values are represented through tokens.

Example:

```css
--spacing-xs;

--spacing-sm;

--spacing-md;

--spacing-lg;

--spacing-xl;

--spacing-2xl;
```

---

# 5. Token Meaning

Tokens should represent usage, not only size.

Example:

```text
xs

Small internal spacing

sm

Compact element separation

md

Default spacing

lg

Section separation

xl

Large layout spacing
```

---

# 6. Component Spacing

Components should define internal spacing using tokens.

Examples:

Buttons:

```text
Icon

↓

Text

↓

Padding
```

Cards:

```text
Header

↓

Content

↓

Actions
```

---

# 7. Layout Spacing

Layout spacing defines relationships between major sections.

Examples:

```text
Navbar

↓

Hero Section

↓

Product Grid

↓

Footer
```

Each section should follow the spacing system.

---

# 8. Container System

The application uses responsive containers.

Containers should:

- adapt to screen size;
- maintain readable content width;
- avoid excessive empty space.

Example:

```text
Mobile

100% width


Tablet

Responsive padding


Desktop

Maximum readable width
```

---

# 9. Grid and Gap System

Grid layouts use spacing tokens.

Example:

```css
gap: var(--spacing-md);
```

Avoid:

```css
gap: 23px;
```

---

# 10. Responsive Spacing

Spacing adapts according to viewport size.

Strategy:

```text
Mobile

Compact spacing

↓

Tablet

Balanced spacing

↓

Desktop

Expanded spacing
```

---

# 11. Ecommerce Usage

Spacing should support ecommerce experiences.

Examples:

## Product Cards

- image spacing;
- title spacing;
- price spacing;
- action spacing.

## Checkout

- form sections;
- payment information;
- confirmation areas.

## Dashboard

- cards;
- tables;
- metrics.

---

# 12. Vertical Rhythm

The interface should maintain predictable vertical relationships.

Examples:

```text
Heading

↓

Description

↓

Action
```

Spacing communicates hierarchy.

---

# 13. Spacing Rules

Developers should:

- use spacing tokens;
- maintain consistency;
- avoid random values;
- prefer reusable patterns.

Avoid:

```css
padding: 19px;
```

Prefer:

```css
padding: var(--spacing-md);
```

---

# 14. Benefits

This spacing system provides:

- consistent layouts;
- faster development;
- better readability;
- easier maintenance;
- professional appearance.

---

# Related Documents

- Design System Overview
- Design Tokens
- Typography
- Responsive System
- Component Library

---

# Document Status

Status: Active

Version: 1.0
