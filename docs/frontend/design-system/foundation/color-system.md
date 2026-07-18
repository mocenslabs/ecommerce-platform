# Color System

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

The Color System defines the complete color architecture used throughout the Premium E-commerce Platform.

Its primary objective is to ensure visual consistency, accessibility and scalability while preventing uncontrolled color usage.

Every color used within the application must originate from the Design Token architecture.

---

# 2. Responsibilities

The Color System is responsible for:

- Defining the primitive color palette.
- Providing semantic color mappings.
- Supporting visual themes.
- Ensuring accessibility.
- Standardizing color usage.
- Eliminating hardcoded colors.
- Simplifying future maintenance.

The Color System does not define component appearance directly.

---

# 3. Design Rationale

Colors represent one of the most frequently repeated values within any user interface.

Allowing components to define their own colors inevitably leads to inconsistency and technical debt.

For this reason, the Design System introduces multiple abstraction layers.

Instead of depending on hexadecimal values, components depend on semantic meaning.

This approach allows the visual identity of the application to evolve without requiring modifications to component implementations.

---

# 4. Color Architecture

The Color System follows a layered architecture.

```
Primitive Palette
        │
        ▼
Theme Tokens
        │
        ▼
Semantic Tokens
        │
        ▼
Component Tokens
```

Each layer has a single responsibility.

Dependencies always flow downward.

Reverse dependencies are prohibited.

---

# 5. Primitive Palette

Primitive Tokens define raw color values.

Examples include:

- Slate
- Cyan
- Emerald
- Amber
- Red
- Sky
- Violet

Each palette provides eleven tonal levels.

```
50
100
200
300
400
500
600
700
800
900
950
```

Primitive Tokens describe appearance only.

They never describe meaning.

---

# 6. Semantic Colors

Semantic Tokens define purpose.

Examples include:

- Primary
- Secondary
- Success
- Warning
- Danger
- Information
- Background
- Surface
- Border
- Text

Components should always consume Semantic Tokens.

Primitive Tokens must remain internal to the Design System.

---

# 7. Theme Integration

Themes redefine Semantic Tokens by remapping Primitive Tokens.

Example:

```
Light Theme

Primary

↓

Cyan 600

Dark Theme

Primary

↓

Cyan 400
```

Because components consume Semantic Tokens, theme changes require no component modifications.

---

# 8. Accessibility

The Color System must support accessible user interfaces.

Guidelines include:

- Sufficient color contrast.
- Visible focus states.
- Color should never be the only communication mechanism.
- Interactive states must remain distinguishable.
- Feedback colors should remain recognizable.

Accessibility takes precedence over visual preference.

---

# 9. Naming Conventions

Token names describe purpose.

Examples:

```
--color-primary

--color-background

--color-text-primary

--color-border

--color-success
```

Avoid implementation-based names such as:

```
--blue

--green

--main-color

--dark-blue
```

Meaning is preferred over appearance.

---

# 10. Usage Rules

All contributors must follow these rules.

Components:

- MUST consume Semantic Tokens.
- MUST NOT consume Primitive Tokens.
- MUST NOT define hexadecimal colors.
- SHOULD remain independent from specific themes.

---

# 11. Best Practices

Recommended practices include:

- Reuse existing Semantic Tokens.
- Keep visual meaning consistent.
- Minimize the creation of new tokens.
- Prefer semantic naming.
- Validate accessibility before introducing new colors.

---

# 12. Forbidden Practices

The following practices are prohibited:

- Hardcoded hexadecimal colors.
- RGB values inside components.
- HSL values inside components.
- Primitive Token consumption.
- Duplicate Semantic Tokens.
- Component-specific color palettes.

Violations should be corrected during code review.

---

# 13. Migration Notes

Future visual redesigns should occur by modifying Theme Tokens rather than component implementations.

If the brand palette changes, components should continue functioning without modification.

This architectural separation minimizes maintenance effort and reduces regression risk.

---

# 14. Future Evolution

Planned improvements include:

- Multiple visual themes.
- High Contrast Theme.
- Seasonal themes.
- Multi-brand support.
- Automated Design Token generation.
- Figma synchronization.
- Style Dictionary integration.

The overall architecture should remain stable.

---

# 15. Related Documents

- README.md
- 02-css-architecture.md
- 03-design-principles.md
- 04-token-architecture.md
- design-tokens.md
