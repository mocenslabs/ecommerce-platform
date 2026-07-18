# Elevation System

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

The Elevation System defines how visual depth is represented throughout the Premium E-commerce Platform.

Its objective is to create a consistent perception of hierarchy while maintaining a clean and modern interface.

All shadows must originate from Design Tokens.

---

# 2. Responsibilities

The Elevation System is responsible for:

- Defining elevation levels.
- Standardizing shadow usage.
- Creating visual hierarchy.
- Supporting accessibility through depth perception.
- Eliminating arbitrary shadow values.

The Elevation System does not replace layout hierarchy or color contrast.

---

# 3. Design Rationale

Elevation communicates relationships between interface elements.

Users naturally perceive elevated elements as interactive or positioned above surrounding content.

A consistent elevation system prevents visual clutter and reinforces the application's spatial model.

Shadows should communicate hierarchy, not decoration.

---

# 4. Architecture

The Elevation System follows a token-based hierarchy.

```
Elevation Tokens
        │
        ▼
Semantic Usage
        │
        ▼
Component Implementation
```

Components consume elevation tokens rather than defining their own shadows.

---

# 5. Elevation Scale

The Design System defines the following elevation levels:

```
--shadow-none
--shadow-xs
--shadow-sm
--shadow-md
--shadow-lg
--shadow-xl
```

Each level represents an increasing perception of depth.

---

# 6. Usage Guidelines

Typical usage includes:

**None**

- Flat sections
- Dividers
- Background containers

**XS**

- Inputs
- Badges
- Chips

**SM**

- Buttons
- Cards
- Small panels

**MD**

- Dropdowns
- Popovers
- Floating toolbars

**LG**

- Sidebars
- Large panels
- Sticky navigation

**XL**

- Modals
- Dialogs
- High-priority overlays

Higher elevation should always imply higher importance.

---

# 7. Visual Hierarchy

Elevation should reinforce interface structure.

Examples:

- Cards should appear above the page background.
- Dropdowns should appear above cards.
- Modals should appear above every standard component.

Visual depth must remain predictable throughout the application.

---

# 8. Naming Conventions

Elevation tokens follow semantic naming.

Examples:

```
--shadow-sm
--shadow-md
--shadow-lg
```

Avoid implementation-specific names such as:

```
--card-shadow
--modal-shadow
```

Shared Design Tokens should always be preferred.

---

# 9. Usage Rules

Components:

- MUST use elevation tokens.
- MUST NOT define custom shadows.
- SHOULD use the minimum elevation required.
- SHOULD preserve a consistent depth hierarchy.

---

# 10. Best Practices

Recommended practices include:

- Prefer subtle shadows.
- Use elevation sparingly.
- Combine elevation with spacing rather than stronger shadows.
- Maintain consistent depth relationships.
- Keep shadows visually unobtrusive.

---

# 11. Forbidden Practices

The following practices are prohibited:

- Hardcoded box-shadow values.
- Decorative shadows without functional purpose.
- Excessive shadow intensity.
- Multiple competing shadow styles.
- Component-specific shadow scales.

---

# 12. Migration Notes

Future visual redesigns should update Design Tokens rather than individual components.

Changing elevation values should automatically propagate throughout the application.

---

# 13. Future Evolution

Future improvements may include:

- Theme-aware elevation.
- Dark mode shadow adjustments.
- Surface tint support.
- CSS Layer integration.
- Adaptive elevation based on interaction state.

The elevation hierarchy should remain stable.

---

# 14. Related Documents

- README.md
- 02-css-architecture.md
- 03-design-principles.md
- 04-token-architecture.md
- design-tokens.md
