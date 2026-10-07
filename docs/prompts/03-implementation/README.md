# Step 03: Implementation

**Goal:** build the confirmed architecture as working, tested code that runs in Docker, with a README.

**Tools:** Claude Code in VS Code with Claude Opus 5.5, in two sessions: a planning session that writes and refines prompts, and a build session that runs them.

## Prompts

| Prompt | Status | Notes |
|---|---|---|
| [v1.0](prompt-v1.0.md) | Not run yet | Written by the planning session at my request, from `docs/architecture.md` version 1.1. This is the prompt for the build session. |

## What the prompt does

1. **It builds the confirmed design and nothing else.** The agent must stop and ask if the design cannot work. It may not redesign.
2. **It sets the order of work,** with a commit after each step: core, adapters and wiring, demo, tests, Docker and scripts, README.
3. **It names the tests.** Each one proves a requirement or a decision by ID, including the two changes from my architecture review (AD9, AD10).
4. **It asks for proof.** The agent has to run the tests and the demo and show the real output, and say plainly if Docker was not verified.
5. **It does not push.** I check the result first.

## Result

Not run yet.
