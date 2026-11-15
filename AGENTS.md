# AGENTS.md

Instructions for any AI agent working in this repo.

## Project
- What it is: <one sentence>
- Stack: <language, framework>
- Run tests: `<command>`
- Run locally: `<command>`

## Workflow rules
1. Every change starts from a GitHub Issue. Work on a branch named `issue-<number>-<short-name>`.
2. Never push to `main`. Open a pull request that references the issue ("Closes #<number>").
3. Run the tests before opening a PR. Add tests for new behavior.
4. Keep PRs small: one issue per PR.
5. Never read, print or commit `.env` files, keys or other secrets.
6. If something is unclear, ask instead of guessing.

## Skills
Reusable skills live in `.skills/`. Before starting a task, check whether a skill
there matches it (each skill's SKILL.md starts with a description of when to use it).
If one matches, read that SKILL.md and follow it.

## Conventions
- <add rules here whenever an agent makes the same mistake twice>
