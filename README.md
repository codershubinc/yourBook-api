# yourBook API

Lightweight NestJS backend service (currently a scaffold) for a future "yourBook" platform (books, collections, or reading tracker). This README documents the existing codebase (Hello World endpoint) and provides a foundation to grow features fast.

![Technology](https://img.shields.io/badge/Node.js-≥18-brightgreen) ![NestJS](https://img.shields.io/badge/NestJS-v11-red) ![Typescript](https://img.shields.io/badge/TypeScript-5.x-blue) ![License](https://img.shields.io/badge/license-UNLICENSED-lightgrey)

## Table of Contents

1. Overview
2. Tech Stack
3. Quick Start
4. Scripts
5. Environment Variables
6. Project Structure
7. API Endpoints
8. Testing
9. Linting & Formatting
10. Build & Run in Production
11. Roadmap (Planned)
12. Contributing
13. License

## 1. Overview

Current state: vanilla NestJS starter (single GET / returning "Hello World!"). This will evolve into the yourBook API. Assumptions (replace later): manage books, authors, shelves, user reading progress.

## 2. Tech Stack

- Runtime: Node.js 18+ (or Bun; `bun.lock` present)
- Framework: NestJS 11
- Language: TypeScript 5
- Testing: Jest (unit + e2e via Supertest)
- Linting: ESLint 9 + Prettier

## 3. Quick Start

Install dependencies (choose one package manager):

```bash
# Using bun (fast - recommended if installed)
bun install

# Or yarn
yarn install

# Or npm
npm install
```

Run in dev watch mode:

```bash
# Bun
bun run start:dev
# Yarn / npm
yarn start:dev
npm run start:dev
```

Open: <http://localhost:3000>

## 4. Scripts

| Script        | Description                          |
| ------------- | ------------------------------------ |
| `start`       | Start app once (no watch)            |
| `start:dev`   | Start with watch mode                |
| `start:debug` | Watch + inspector                    |
| `start:prod`  | Run compiled dist (`node dist/main`) |
| `build`       | Compile TypeScript to `dist/`        |
| `test`        | Run unit tests                       |
| `test:e2e`    | Run e2e tests (`test/jest-e2e.json`) |
| `test:cov`    | Coverage report                      |
| `lint`        | ESLint fix mode                      |
| `format`      | Prettier write                       |

With Bun you can run the same scripts: `bun run test` etc.

## 5. Environment Variables

| Variable | Default | Purpose            |
| -------- | ------- | ------------------ |
| `PORT`   | 3000    | HTTP listener port |

Add a `.env` file (not committed) if you expand configuration later.

## 6. Project Structure

```text
src/
  main.ts            # App bootstrap (reads PORT)
  app.module.ts      # Root module
  app.controller.ts  # GET /
  app.service.ts     # Simple service
test/
  app.e2e-spec.ts    # Example e2e test
```

## 7. API Endpoints (Current)

| Method | Path | Description         | Example Response |
| ------ | ---- | ------------------- | ---------------- |
| GET    | /    | Health/example root | `Hello World!`   |

Example curl:

```bash
curl -i http://localhost:3000/
```

## 8. Testing

Unit tests (specs inside `src/`):

```bash
yarn test        # or bun run test / npm test
```

E2E tests:

```bash
yarn test:e2e
```

Coverage:

```bash
yarn test:cov
```

Reports output to `coverage/`.

## 9. Linting & Formatting

```bash
yarn lint      # ESLint (auto-fix)
yarn format    # Prettier format
```

CI suggestion: run `yarn lint && yarn test:cov` on pull requests.

## 10. Build & Run in Production

```bash
yarn build
PORT=8080 yarn start:prod
```

Creates `dist/` then runs compiled JavaScript. Containerization suggestion (future): multi-stage Docker build (builder + runtime slim image).

## 11. Roadmap (Planned)

- [ ] Book entity CRUD
- [ ] Author profiles
- [ ] User authentication & JWT
- [ ] Shelves / collections
- [ ] Reading progress tracking
- [ ] Search & pagination
- [ ] OpenAPI (Swagger) docs (`@nestjs/swagger`)
- [ ] Docker image + CI pipeline

## 12. Contributing

1. Fork & branch (`feat/<name>`)
2. Keep commits small & conventional (`feat: add book entity`)
3. Add/update tests for changes
4. Run lint & tests before PR

## 13. License

Currently `UNLICENSED` (closed source). If you intend to open source, choose a license (MIT, Apache-2.0, etc.) and update `package.json` + this section.

---

Replace assumptions above as features are implemented.
