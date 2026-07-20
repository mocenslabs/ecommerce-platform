# Component Tokens

## Overview

The Component Tokens layer defines the visual contract for every UI component.

Unlike Design Tokens, which represent global design decisions, Component Tokens translate those decisions into component-specific variables.

Components consume Component Tokens instead of Foundation Tokens directly.

---

# Architecture

```
Foundation Tokens
        │
        ▼
Semantic Tokens
        │
        ▼
Component Tokens
        │
        ▼
Vue Components
```

---

# Responsibility

This layer is responsible for defining:

- Component spacing
- Component sizing
- Component colors
- Component borders
- Component elevation
- Component typography
- Component motion

without implementing component styles.

---

# What belongs here

Examples:

- Button tokens
- Input tokens
- Card tokens
- Modal tokens
- Badge tokens

---

# What DOES NOT belong here

The following items are prohibited:

- CSS classes
- Component layouts
- HTML styling
- Business logic
- Vue specific code
- Component implementations

---

# Directory Structure

```
component-tokens/

forms/

feedback/

navigation/

overlays/

surfaces/
```

Each module groups related UI components.

---

# Rules

- Components consume Component Tokens.
- Component Tokens consume Design Tokens.
- Component Tokens must remain implementation agnostic.
- One file per component.
- Never define CSS classes.
- Never duplicate Design Tokens.

---

# Naming Convention

Variables follow this convention:

```
--button-padding-x

--button-padding-y

--button-radius

--button-background

--button-border
```

Each component owns its visual contract.

---

# Dependency Flow

```
Foundation Tokens

↓

Semantic Tokens

↓

Component Tokens

↓

Vue Components
```

Dependencies are one-directional.

---

# Maintenance Notes

Before introducing new tokens:

- Verify that a similar token does not already exist.
- Reuse Foundation Tokens whenever possible.
- Avoid component duplication.
- Keep naming consistent.
- Prefer composition over specialization.
