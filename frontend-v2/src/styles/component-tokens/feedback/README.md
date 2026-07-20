# Feedback Component Tokens

## Overview

Defines the visual contract for feedback-related components.

These components communicate application state, system responses and user notifications.

---

# Components

- Alert
- Badge
- Chip
- Toast
- Spinner
- Skeleton

---

# Rules

Each file:

- defines only CSS variables
- contains no CSS classes
- contains no layouts
- contains no component implementation

---

# Dependency Flow

Foundation Tokens

↓

Semantic Tokens

↓

Feedback Component Tokens

↓

Vue Components

---

# Naming Convention

--alert-*

--badge-*

--chip-*

--toast-*

--spinner-*

--skeleton-*

---

# Maintenance Notes

Each feedback component owns its own namespace.

Do not duplicate Foundation or Semantic Tokens.

Prefer semantic colors over primitive palette values.
