# Contributing to Davarus Bell Platform

Thank you for your interest in contributing to the **Davarus Bell Platform** engineered by **RJ Business Solutions**.

## Development Principles & Rules

1. **Evidence Before Assertion:** Always verify runtime behavior before asserting clean builds or test completions.
2. **Deterministic Before Generative:** Prefer reliable code and static optimizations over unnecessary generative calls.
3. **Cloudflare-First Architecture:** Platform compute must rely on Cloudflare Workers, Hono runtime, and D1 SQLite persistence.
4. **TREC & Fair Housing Compliance:** All real estate copy and landing page elements must follow strict Texas Real Estate Commission (TREC) guidelines and Fair Housing Act standards.

## Commit Message Format

We follow the Conventional Commits specification:

```
<type>(<scope>): <short description>
```

Types:
* `feat`: A new feature or funnel route
* `fix`: A bug fix or compliance correction
* `docs`: Documentation updates (README, ADRs, specs)
* `style`: Styling adjustments (Tailwind CSS, typography)
* `refactor`: Code restructuring without functional changes
* `perf`: Performance or asset size optimizations
* `test`: Adding or updating test suites
* `chore`: Maintenance, dependencies, or Wrangler updates

Example: `feat(api): add D1 lead capture endpoint for ITIN buyers`

## Development Setup

```bash
git clone https://github.com/rjbizsolution23-wq/davarus-bell-platform.git
cd davarus-bell-platform/app
npm install
npx tsc --noEmit
```
