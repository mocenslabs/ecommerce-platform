# Forms Component Tokens

## Overview

Defines the visual contract for all form-related components.

This module centralizes every token required by interactive form controls.

---

# Components

- Button
- Input
- Textarea
- Select
- Checkbox
- Radio
- Switch

---

# Rules

Each file:

- defines only CSS variables
- contains no CSS classes
- contains no layouts
- contains no component implementations

---

# Dependency Flow

```
Foundation Tokens

↓

Semantic Tokens

↓

Forms Component Tokens

↓

Vue Components
```

---

# Naming Convention

```
--button-*

--input-*

--textarea-*

--select-*

--checkbox-*

--radio-*

--switch-*
```

---

# Maintenance Notes

Each component owns its own namespace.

Avoid sharing variables between unrelated components.

When multiple components require the same value, consume Foundation Tokens instead of duplicating variables.
