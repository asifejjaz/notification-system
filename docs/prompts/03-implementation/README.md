# Step 03: Implementation

**Goal:** build the confirmed architecture as working, tested code that runs in Docker, with a README.

**Tools:** Claude Code in VS Code with Claude Opus 5.5, in two sessions: a planning session that writes and refines prompts, and a build session that runs them.

## Prompts

| Prompt | Status | Notes |
|---|---|---|
| [v1.0](prompt-v1.0.md) | Run | Written by the planning session at my request, from `docs/architecture.md` version 1.1. Run in the build session. |

## What the prompt does

1. **It builds the confirmed design and nothing else.** The agent must stop and ask if the design cannot work. It may not redesign.
2. **It sets the order of work,** with a commit after each step: core, adapters and wiring, demo, tests, Docker and scripts, README.
3. **It names the tests.** Each one proves a requirement or a decision by ID, including the two changes from my architecture review (AD9, AD10).
4. **It asks for proof.** The agent has to run the tests and the demo and show the real output, and say plainly if Docker was not verified.
5. **It does not push.** I check the result first.

## Result

- The build session wrote the code in six commits, in the order the prompt set: core, adapters and wiring, demo, tests, Docker and scripts, README.
- Output: the `notification_system` package, 23 tests, the Dockerfile, the build, run and test scripts, and the root [README.md](../../../README.md).

## My review

I asked the planning session to review the implementation against the architecture. It read the code and ran it independently of the build session's report:

- 23 tests passed on local Python 3.11 and inside the container on Python 3.13.
- The image built, and the demo output matched the README.
- Every approval and every review change from step 02 was implemented and tested.

It found two things in the code. I acted on one:

- **Added:** a compile step. The brief says the product must compile and run, so the Dockerfile now compiles every module and the build fails on a syntax error. The planning session made this change and ran the build, the tests and the demo again.
- **Left as it is:** if one event has two rules and the first one fails, the second does not run. No event has two rules today, so I noted it and did not change it.
