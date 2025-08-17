# Backlog & Roadmap

Priority legend:
- P0 = Must do next (critical foundation)
- P1 = Important (next after P0s)
- P2 = Nice-to-have / polish

Label legend:
- area:auth, area:posts, area:tests, area:migrations, area:dx, area:infra, area:deploy
- type:feature, type:chore, type:bug

---

## P0 – Core Foundation

### Ticket: Expand test coverage for user routes
**Labels:** P0, area:tests, type:feature  
**Body:**
- Add tests for user signup success and failures:
  - [ ] duplicate email returns 409/400 (whichever your API uses)
  - [ ] invalid email returns 422
  - [ ] password min length enforced (if applicable)
- [ ] Create pytest fixtures for fake users
- [ ] Ensure tests use **separate Postgres test DB** via `conftest.py` override
**Acceptance Criteria:**
- [ ] `pytest -v` passes locally
- [ ] Tests are isolated (no dependency on run order)

---

### Ticket: Implement JWT Authentication
**Labels:** P0, area:auth, area:tests, type:feature  
**Body:**
- [ ] Add login endpoint that returns `access_token` (JWT) + `token_type=bearer`
- [ ] Protect private routes with dependency (e.g., `get_current_user`)
- [ ] Write tests for login success/failure and a protected route (401/403 when missing/invalid)
**Acceptance Criteria:**
- [ ] Login works and returns JWT
- [ ] Protected route denies unauthenticated requests
- [ ] Tests cover both success and failure paths

---

### Ticket: Posts CRUD with ownership rules
**Labels:** P0, area:posts, area:tests, type:feature  
**Body:**
- [ ] Create `Post` model linked to `User` (FK owner_id)
- [ ] Routes: create, list (with pagination), get by id, update, delete
- [ ] Only owner can update/delete their post (403 otherwise)
- [ ] Tests for all endpoints incl. ownership checks
**Acceptance Criteria:**
- [ ] CRUD works end-to-end with JWT auth
- [ ] Ownership rules enforced
- [ ] Tests green

---

## P1 – Industry Essentials

### Ticket: Role-Based Access Control (RBAC)
**Labels:** P1, area:auth, area:tests, type:feature  
**Body:**
- [ ] Introduce roles (`user`, `admin`)
- [ ] Restrict admin-only routes (e.g., list all users, delete any post)
- [ ] Tests for RBAC (user vs admin access)
**Acceptance Criteria:**
- [ ] Role stored in DB / token claims
- [ ] RBAC enforced in endpoints
- [ ] Tests green

---

### Ticket: Alembic migrations setup
**Labels:** P1, area:migrations, type:chore  
**Body:**
- [ ] Install & init Alembic
- [ ] Configure SQLAlchemy URL from env
- [ ] Generate initial migration for current models
- [ ] Document commands: `alembic revision --autogenerate -m "..."`, `alembic upgrade head`
**Acceptance Criteria:**
- [ ] New dev can run migrations from scratch
- [ ] No manual table creation required

---

### Ticket: Integration tests for core flows
**Labels:** P1, area:tests, type:feature  
**Body:**
- [ ] Flow: signup → login → create post → list → update → delete
- [ ] Use fixtures for token/auth header
- [ ] Ensure DB isolation
**Acceptance Criteria:**
- [ ] One or more tests cover the full happy path
- [ ] Green in CI (later)

---

## P1 – Developer Experience

### Ticket: Logging setup (structured)
**Labels:** P1, area:dx, type:chore  
**Body:**
- [ ] Configure Python `logging` (request ID, level, timestamp)
- [ ] Add error logs for exceptions
- [ ] Optional: JSON logs for prod
**Acceptance Criteria:**
- [ ] Logs visible in console
- [ ] Errors include stack trace

---

### Ticket: Pre-commit hooks (black, isort, flake8)
**Labels:** P1, area:dx, type:chore  
**Body:**
- [ ] Add `.pre-commit-config.yaml` with black, isort, flake8
- [ ] `pre-commit install`
- [ ] Fix existing style issues
**Acceptance Criteria:**
- [ ] Commits auto-format/lint
- [ ] CI (later) runs `flake8`

---

### Ticket: Dockerize app and DB
**Labels:** P1, area:infra, type:feature  
**Body:**
- [ ] Add `Dockerfile` for FastAPI app (uvicorn)
- [ ] Add `docker-compose.yml` with Postgres
- [ ] Healthcheck and `.env` support
- [ ] Update README with `docker compose up`
**Acceptance Criteria:**
- [ ] App + DB run locally via Docker
- [ ] README instructions work fresh

---

## P2 – Deployment & Polish

### Ticket: GitHub Actions CI (pytest on push/PR)
**Labels:** P2, area:deploy, area:tests, type:chore  
**Body:**
- [ ] Workflow: setup Python, install deps, run `pytest`
- [ ] Cache pip
- [ ] (Optional) report coverage
**Acceptance Criteria:**
- [ ] CI is green on `main` and PRs
- [ ] Badges (optional) in README

---

### Ticket: Deploy to Render/railway (free tier) or Fly.io
**Labels:** P2, area:deploy, type:feature  
**Body:**
- [ ] Container-based deploy
- [ ] Provision managed Postgres
- [ ] Set env vars
- [ ] Add “Live demo” link to README
**Acceptance Criteria:**
- [ ] Public URL serves app
- [ ] `/docs` accessible

---

### Ticket: Password reset & email verification (optional)
**Labels:** P2, area:auth, type:feature  
**Body:**
- [ ] Add email verification flow
- [ ] Password reset token + endpoint
- [ ] (Optional) Background task for sending email
**Acceptance Criteria:**
- [ ] Flows tested (unit/integration)
- [ ] Security reviewed

---
