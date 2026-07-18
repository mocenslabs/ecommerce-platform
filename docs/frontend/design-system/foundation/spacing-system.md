# Spacing System

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

The Spacing System defines the official spacing scale used throughout the Premium E-commerce Platform.

Its purpose is to establish consistent spacing relationships between interface elements while eliminating arbitrary spacing decisions.

All margins, paddings and gaps must be defined using Design Tokens.

---

# 2. Responsibilities

The Spacing System is responsible for:

- Defining a consistent spacing scale.
- Standardizing layout spacing.
- Standardizing component spacing.
- Supporting responsive layouts.
- Eliminating hardcoded spacing values.
- Improving visual rhythm.
- Simplifying maintenance.

The Spacing System does not define component layouts.

---

# 3. Design Rationale

Consistent spacing improves readability, usability and visual balance.

When spacing values are chosen arbitrarily, interfaces quickly become inconsistent and difficult to maintain.

A shared spacing scale creates predictable relationships between elements and significantly reduces visual noise.

The Design System adopts a spacing architecture based on reusable Design Tokens rather than fixed values inside components.

---

# 4. Architecture

The spacing architecture follows a simple hierarchy.

```
Spacing Scale
        │
        ▼
Semantic Usage
        │
        ▼
Component Implementation
```

Spacing values are defined once and reused everywhere.

---

# 5. Spacing Scale

The Design System follows a **4px baseline grid**.

Each spacing token represents a multiple of this base unit.

Examples include:

```
--space-0

--space-1

--space-2

--space-3

--space-4

--space-5

--space-6

--space-8

--space-10

--space-12

--space-16

--space-20

--space-24

--space-32
```

This scale provides sufficient flexibility while maintaining consistency.

---

# 6. Usage Guidelines

Spacing tokens should be used for:

- Padding
- Margin
- Gap
- Grid spacing
- Section spacing
- Component spacing
- Layout spacing

Spacing should communicate hierarchy and improve readability.

---

# 7. Responsive Considerations

Spacing should scale naturally across different layouts.

Larger viewports may increase spacing between major layout sections, while preserving the overall spacing rhythm.

Responsive adjustments should remain proportional to the established spacing scale.

---

# 8. Naming Conventions

Spacing tokens follow a numeric naming convention.

Examples:

```
--space-1

--space-2

--space-4

--space-8

--space-16
```

Numbers represent the predefined spacing scale and should never imply specific UI elements.

---

# 9. Usage Rules

All contributors must follow these rules.

Components:

- MUST use spacing tokens.
- MUST NOT use arbitrary pixel values.
- SHOULD reuse existing spacing values.
- SHOULD maintain consistent spacing relationships.

---

# 10. Best Practices

Recommended practices include:

- Use the smallest spacing that satisfies readability.
- Maintain consistent spacing between similar elements.
- Reuse spacing patterns across components.
- Prefer existing tokens over creating new ones.
- Keep layouts visually balanced.

---

# 11. Forbidden Practices

The following practices are prohibited:

- Hardcoded spacing values.
- Random pixel values.
- Mixing spacing systems.
- Component-specific spacing scales.
- Negative spacing without documented justification.

Spacing inconsistencies should be corrected during review.

---

# 12. Migration Notes

Future adjustments to spacing should occur by updating Design Tokens rather than individual components.

Because every component consumes spacing tokens, global refinements can be introduced with minimal implementation changes.

---

# 13. Future Evolution

Planned improvements include:

- Semantic spacing aliases.
- Density modes.
- Compact layouts.
- Comfortable layouts.
- Adaptive spacing based on container size.
- Container Query integration.

The spacing scale itself should remain stable.

---

# 14. Related Documents

- README.md
- 02-css-architecture.md
- 03-design-principles.md
- 04-token-architecture.md
- design-tokens.md
