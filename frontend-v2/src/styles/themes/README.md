# Themes

## Overview

The Theme layer defines the visual identity of the application.

Themes never introduce new design decisions.

Instead, they map Semantic Design Tokens to values appropriate for a particular visual experience (Light, Dark, High Contrast, Brand Themes, etc.).

---

# Architecture

```
Primitive Colors
        ↓
Semantic Tokens
        ↓
Theme
        ↓
Components
```

Components must never consume Primitive Colors directly.

Components should consume Theme variables.

---

# Directory Structure

```text
themes/

├── index.css
├── light.css
├── dark.css
└── README.md
```

---

# Responsibilities

The Theme layer is responsible for:

- Brand colors
- Backgrounds
- Surface colors
- Text colors
- Border colors
- Status colors

It is **not** responsible for:

- Layout
- Typography hierarchy
- Spacing
- Animations
- Component styling

Those responsibilities belong to other architecture layers.

---

# Default Theme

The application ships with the Light Theme enabled.

```css
@import "./light.css";
```

---

# Dark Theme

The Dark Theme is already implemented but remains disabled until runtime theme switching is introduced.

Example:

```html
<html data-theme="dark">
```

---

# Future Themes

The architecture supports unlimited themes.

Examples:

- Dark
- High Contrast
- Christmas
- Black Friday
- Client Branding
- Seasonal Themes

No component changes are required when adding new themes.

---

# Best Practices

✔ Components consume Theme variables.

✔ Themes consume Semantic Tokens.

✔ Semantic Tokens consume Primitive Colors.

Never skip a layer.

---

# Maintenance Notes

When adding a new theme:

1. Create a new CSS file.
2. Map Semantic Tokens.
3. Import the theme inside `index.css`.
4. Do not modify existing components.
