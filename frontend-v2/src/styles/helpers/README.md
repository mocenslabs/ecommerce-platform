# Helpers

## Overview

The Helpers layer provides reusable CSS resources shared across the application.

Unlike Utilities, Helpers are **not** intended to be composed directly to build layouts or components.

Instead, they provide reusable building blocks such as animations and keyframes.

---

## Responsibilities

Helpers may contain:

- CSS animations
- CSS keyframes
- Future reusable animation resources

Helpers must **not** contain:

- Layout utilities
- Typography utilities
- Component styles
- Design Tokens
- Theme definitions

---

## Architecture

```
Tokens
    ↓
Base
    ↓
Themes
    ↓
Utilities
    ↓
Helpers
    ↓
Components
```

---

## Files

| File | Responsibility |
|------|----------------|
| keyframes.css | Defines reusable CSS keyframes |
| animations.css | Defines reusable animation helper classes |

---

## Rules

- Helpers must remain generic.
- Components may consume helper classes.
- Helpers must never define component-specific animations.
- Animation durations must consume Motion Tokens whenever possible.
- Helpers must not contain business logic.
