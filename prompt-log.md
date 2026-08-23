# Prompt Log

A running record of AI sessions that mattered — what I asked, what it got wrong, how I caught it.

## 2026-08-22 — Portfolio repo setup
- **Tool:** Claude
- **What I asked:** Help setting up the Stage 0 portfolio repo skeleton (AGENTS.md,
  CLAUDE.md, .gitignore, prompt-log.md, folder structure).
- **What it got right/wrong:** Claude built the Stage 0 skeleton correctly overall, but misplaced AGENTS.md, CLAUDE.md, .gitignore, and prompt-log.md inside docs/decisions/ instead of the repo root.
- **How I caught it:** I went back and checked its work myself and noticed some files were in the wrong folders.
