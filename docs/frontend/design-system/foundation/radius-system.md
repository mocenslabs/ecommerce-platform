# Radius System

---

## Document Information

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Status | Approved |
| Last Updated | 2026-07-17 |
| Author | Mocens Labs |
| Audience | Frontend Developers, UI Designers, Software Architects, Contributors |

---

# 1. Purpose

The Radius System defines the official border radius architecture used throughout the Premium E-commerce Platform.

Its objective is to provide a consistent visual language by standardizing corner rounding across all interface elements.

Every border radius must originate from Design Tokens.

---

# 2. Responsibilities

The Radius System is responsible for:

- Defining the official border radius scale.
- Standardizing component appearance.
- Supporting visual consistency.
- Eliminating arbitrary radius values.
- Simplifying future visual updates.

The Radius System does not define component shape or layout behavior.

---

# 3. Design Rationale

Border radius has a significant impact on the perceived personality of an interface.

A consistent radius scale creates a cohesive visual identity and improves the overall user experience.

Centralizing radius values into Design Tokens allows the visual style of the application to evolve without modifying component implementations.

---

# 4. Radius Architecture

The Radius System consists of a predefined scale.

```
Radius Tokens
        │
        ▼
Semantic Usage
        │
        ▼
Component Implementation
```

Components consume radius tokens rather than hardcoded values.

---

# 5. Radius Scale

The Design System defines the following radius tokens:

```
--radius-none
--radius-xs
--radius-sm
--radius-md
--radius-lg
--radius-xl
--radius-full
```

Each token has a specific purpose within the visual hierarchy.

---

# 6. Usage Guidelines

Typical usage includes:

**None**

- Dividers
- Tables
- Flat layouts

**XS / SM**

- Small badges
- Chips
- Compact controls

**MD**

- Buttons
- Inputs
- Selects
- Cards

**LG / XL**

- Modals
- Large containers
- Promotional banners

**Full**

- Avatars
- Circular buttons
- Status indicators

---

# 7. Visual Consistency

Components serving similar purposes should share the same border radius.

For example:

- Every primary button should use the same radius.
- Every text input should use the same radius.
- Every card variant should remain visually consistent.

This predictability strengthens the visual identity of the application.

---

# 8. Naming Conventions

Radius tokens should follow semantic naming.

Examples:

```
--radius-sm
--radius-md
--radius-lg
```

Avoid implementation-specific names such as:

```
--button-radius
--card-radius
```

Components should reuse shared Design Tokens.

---

# 9. Usage Rules

Components:

- MUST use radius tokens.
- MUST NOT define hardcoded radius values.
- SHOULD reuse existing tokens.
- SHOULD maintain consistency across similar components.

---

# 10. Best Practices

Recommended practices include:

- Prefer the smallest radius that satisfies the design.
- Reuse existing tokens whenever possible.
- Maintain consistent rounding across similar UI elements.
- Reserve large radius values for emphasis.

---

# 11. Forbidden Practices

The following practices are prohibited:

- Hardcoded border radius values.
- Component-specific radius scales.
- Inconsistent rounding between similar components.
- Introducing new radius values without architectural review.

---

# 12. Migration Notes

Future visual redesigns should modify Design Tokens instead of individual components.

Changing the radius scale should automatically propagate throughout the application while preserving component implementations.

---

# 13. Future Evolution

Future improvements may include:

- Density modes.
- Brand-specific radius themes.
- Platform-specific radius presets.
- Additional semantic radius tokens if justified.

The core radius scale should remain stable.

---

# 14. Related Documents

- README.md
- 02-css-architecture.md
- 03-design-principles.md
- 04-token-architecture.md
- design-tokens.md
