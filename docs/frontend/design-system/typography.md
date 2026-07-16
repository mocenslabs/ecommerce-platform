# Typography System

## Document Information

| Field         | Value                       |
|---------------|-----------------------------|
| Document Name | Typography System           |
| Version       | 1.0                         |
| Status        | Active                      |
| Area          | Frontend Engineering        |
| Scope         | Premium E-commerce Platform |
| Last Updated  | 2026-07-14                  |

---

# 1. Purpose

This document defines the typography system used by the frontend Design System.

Typography establishes hierarchy, readability, and visual identity across the application.

---

# 2. Typography Philosophy

Typography should provide:

- clarity;
- hierarchy;
- accessibility;
- consistency;
- professional appearance.

Text styles should be intentional and reusable.

---

# 3. Font Strategy

The application should use a limited number of font families.

The default approach:

```text
One primary font family

+

Optional specialized fonts when justified
```

Avoid unnecessary font variations.

---

# 4. Font Family

Typography tokens should centralize font definitions.

Example:

```css
--font-family-primary;

--font-family-heading;

--font-family-monospace;
```

---

# 5. Font Weight System

The system uses predefined font weights.

Example:

```css
--font-weight-regular;

--font-weight-medium;

--font-weight-semibold;

--font-weight-bold;
```

Font weights should be used consistently.

---

# 6. Type Scale

The application follows a structured type scale.

Example:

```text
Display

↓

Heading

↓

Subtitle

↓

Body

↓

Caption

↓

Small Text
```

---

# 7. Heading Styles

Headings define page hierarchy.

Example:

```text
H1

Main page title

H2

Section title

H3

Component title

H4

Supporting title
```

Each heading level should have a clear purpose.

---

# 8. Body Text

Body typography is optimized for readability.

Used for:

- descriptions;
- product information;
- instructions;
- general content.

Body text should prioritize:

- readable size;
- comfortable line height;
- sufficient contrast.

---

# 9. Caption and Supporting Text

Smaller text is used for:

- metadata;
- timestamps;
- secondary information.

Small text should not contain critical information.

---

# 10. Typography Tokens

Typography values should be centralized.

Examples:

```css
--text-display;

--text-heading-xl;

--text-heading-lg;

--text-body;

--text-caption;
```

---

# 11. Line Height

Line height improves readability.

Tokens should define:

```css
--line-height-tight;

--line-height-normal;

--line-height-relaxed;
```

---

# 12. Letter Spacing

Letter spacing should be used carefully.

Possible uses:

- uppercase labels;
- navigation items;
- special headings.

Avoid excessive customization.

---

# 13. Responsive Typography

Typography must adapt across devices.

The strategy follows:

```text
Mobile

↓

Tablet

↓

Desktop

↓

Large Desktop
```

Large screens may increase hierarchy while preserving readability.

---

# 14. Ecommerce Typography Usage

Typography should support:

## Products

- product name;
- price;
- discount;
- availability.

## Checkout

- steps;
- totals;
- confirmation messages.

## Dashboard

- metrics;
- tables;
- notifications.

---

# 15. Accessibility Considerations

Typography must consider:

- readable sizes;
- sufficient contrast;
- proper hierarchy;
- screen reader compatibility.

---

# 16. Typography Rules

Developers should:

- use predefined typography tokens;
- avoid arbitrary sizes;
- maintain hierarchy;
- prioritize readability.

Avoid:

```css
font-size: 37px;
```

Prefer:

```css
font-size: var(--text-heading-xl);
```

---

# 17. Benefits

This typography system provides:

- consistent hierarchy;
- better readability;
- faster development;
- professional visual identity.

---

# Related Documents

- Design System Overview
- Design Tokens
- Color System
- Spacing System
- Accessibility

---

# Document Status

Status: Active

Version: 1.0
