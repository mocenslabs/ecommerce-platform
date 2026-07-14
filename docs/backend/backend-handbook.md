# Backend Handbook

## Purpose

This handbook serves as the primary technical reference for backend development.

---

# Architecture

The backend follows a modular architecture based on Django applications.

Each application owns a single business domain.

---

# Design Principles

- Separation of concerns
- Domain ownership
- Service Layer
- Thin Views
- Reusable serializers
- Shared infrastructure through Core

---

# Coding Standards

- Black
- Ruff
- isort
- Type hints where applicable

---

# API Principles

- RESTful endpoints
- Versioned API
- JWT Authentication
- Standardized responses

---

# Database

- PostgreSQL in production
- SQLite for local development

---

# Testing

- pytest
- Factory Boy
- Coverage reports

---

# Deployment

- Docker
- Docker Compose
- GitHub Actions
- Fly.io

---

# Documentation

All architectural decisions must be documented.

Every new application requires:

- API Reference
- Technical Audit
- Business Rules update
