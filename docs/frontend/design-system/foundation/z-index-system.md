# Z-Index System

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

The Z-Index System defines the official layering architecture used throughout the Premium E-commerce Platform.

Its objective is to establish a predictable stacking order for interface elements while preventing layering conflicts.

Every z-index value must originate from Design Tokens.

---

# 2. Responsibilities

The Z-Index System is responsible for:

- Defining stacking layers.
- Standardizing visual hierarchy.
- Preventing z-index conflicts.
- Supporting overlays and floating elements.
- Eliminating arbitrary z-index values.

The Z-Index System does not replace proper document flow or layout structure.

---

# 3. Design Rationale

As applications grow, independently assigned z-index values quickly become difficult to maintain.

Without a shared layering strategy, components compete for visual priority, resulting in unpredictable behavior.

A centralized Z-Index System guarantees consistency and simplifies long-term maintenance.

---

# 4. Layering Architecture

The Design System organizes layers from lowest to highest priority.

```
Base Content
        │
        ▼
Sticky Elements
        │
        ▼
Dropdowns
        │
        ▼
Floating Components
        │
        ▼
Overlays
        │
        ▼
Modals
        │
        ▼
Notifications
        │
        ▼
Tooltips
```

Each layer has a clearly defined responsibility.

---

# 5. Layer Definitions

Typical layers include:

**Base**

- Standard page content.

**Sticky**

- Sticky headers.
- Sticky navigation.

**Dropdown**

- Menus.
- Select options.
- Context menus.

**Floating**

- Floating action buttons.
- Popovers.
- Floating panels.

**Overlay**

- Background overlays.
- Loading overlays.

**Modal**

- Dialogs.
- Confirmation windows.

**Notification**

- Toast messages.
- Global alerts.

**Tooltip**

- Tooltips.
- Guided tours.

Higher layers should always appear above lower layers.

---

# 6. Token Usage

The Design System exposes semantic z-index tokens.

Examples include:

```
--z-base
--z-sticky
--z-dropdown
--z-floating
--z-overlay
--z-modal
--z-notification
--z-tooltip
```

Components must consume these tokens rather than defining numeric values.

---

# 7. Naming Conventions

Layer names describe purpose rather than implementation.

Examples:

```
--z-modal
--z-overlay
--z-tooltip
```

Avoid names such as:

```
--z-9999
--top-layer
--highest
```

Semantic naming improves readability and maintainability.

---

# 8. Usage Rules

Components:

- MUST use z-index tokens.
- MUST NOT define numeric z-index values.
- SHOULD use the lowest layer that satisfies the requirement.
- SHOULD preserve the established stacking hierarchy.

---

# 9. Best Practices

Recommended practices include:

- Keep the number of layers small.
- Reuse existing layer tokens.
- Avoid unnecessary stacking contexts.
- Review visual hierarchy before introducing new layers.
- Prefer structural solutions before increasing z-index.

---

# 10. Forbidden Practices

The following practices are prohibited:

- Hardcoded z-index values.
- Magic numbers.
- Competing overlay hierarchies.
- Component-specific z-index scales.
- Creating new layers without architectural review.

Layering decisions should always be intentional.

---

# 11. Migration Notes

Future adjustments to the stacking order should be implemented by modifying Design Tokens rather than individual components.

A centralized layering system minimizes conflicts and simplifies maintenance.

---

# 12. Future Evolution

Planned improvements include:

- Top Layer API support.
- Native Popover API integration.
- View Transition layering.
- Cross-window overlay management.
- Advanced portal architecture.

The semantic layer hierarchy should remain stable.

---

# 13. Related Documents

- README.md
- 02-css-architecture.md
- 03-design-principles.md
- 04-token-architecture.md
- design-tokens.md
