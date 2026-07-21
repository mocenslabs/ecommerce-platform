# Contributing Guide

## Overview

This document defines the engineering standards for contributing to the Premium E-commerce Platform Design System.

Every modification to the Design System must follow these guidelines to preserve consistency, maintainability and scalability.

The Design System is considered a shared architectural asset rather than a collection of CSS files.

---

# Design Principles

Every contribution should follow these principles.

## Consistency

Prefer existing tokens before creating new ones.

Avoid introducing duplicate concepts.

---

## Reusability

Design tokens should solve multiple use cases.

Component Tokens should never solve application-specific problems.

---

## Predictability

Files should always follow the same structure.

Documentation should remain consistent across the project.

---

## Accessibility

Every new component must support accessibility requirements.

Accessibility should never be considered optional.

---

## Simplicity

Prefer extending the current architecture instead of creating new layers.

Avoid unnecessary abstractions.

---

# Folder Responsibilities

## Foundation

Defines primitive design decisions.

Examples:

- colors
- spacing
- typography
- radius
- elevation
- motion

---

## Themes

Defines application themes.

Example:

- light
- dark

---

## Utilities

Reusable utility classes.

Utilities never contain component-specific styles.

---

## Helpers

Reusable CSS helpers.

Helpers never define visual appearance.

---

## Component Tokens

Defines the visual contract for components.

Contains only CSS Custom Properties.

Never contains implementation.

---

# Component Token Rules

Every new component must:

- use the Golden Template
- consume Foundation Tokens
- consume Semantic Tokens
- avoid hardcoded values
- include Maintenance Notes
- follow the official naming convention

---

# Naming Rules

CSS variables must follow:

--component-property

Example:

--button-padding

--card-radius

--modal-shadow

Avoid abbreviations.

Avoid generic names.

---

# Documentation Rules

Every file must contain:

- Header
- Responsibility
- Rules
- Notes
- Section documentation
- Maintenance Notes

Documentation should always be written in English.

---

# Pull Request Checklist

Before submitting changes verify:

- Foundation Tokens reused whenever possible.
- Semantic Tokens reused whenever possible.
- No duplicated variables.
- No hardcoded colors.
- No hardcoded spacing.
- No hardcoded typography.
- Documentation updated.
- Manifest updated.
- CHANGELOG updated if required.

---

# Architecture Changes

Structural modifications require reviewing:

- dependency flow
- folder responsibilities
- naming conventions
- documentation

Architecture changes should be exceptional.

---

# Versioning

Breaking architectural changes should only occur in major Design System versions.

Minor releases should remain backward compatible whenever possible.

---

# Code Review

Every contribution should answer:

1. Can an existing token solve this?

2. Is this component generic?

3. Is the naming consistent?

4. Does this duplicate another concept?

5. Will this scale in one year?

If any answer is negative, reconsider the implementation.

---

# Final Principle

The Design System should evolve through deliberate architectural decisions rather than incremental patches.

Every contribution should leave the system clearer, simpler and more maintainable than before.
