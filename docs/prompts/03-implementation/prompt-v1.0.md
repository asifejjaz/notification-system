# Step 03: Implementation (prompt v1.0)

**Status:** written by the planning session at my request. Run in the build session on 2026-10-07. The [step README](README.md) has the result.

```text
This is step 03: implementation. Steps 01 and 02 are done and confirmed.

Read docs/architecture.md (version 1.1, CONFIRMED) and docs/requirements.md (version 1.1)
in the notification-system repo. Build exactly that design: the modules in section 7, the
entities in section 4, the decisions AD1 to AD11 and the choices in section 9. If part of
the design cannot work, stop and tell me. Don't redesign it yourself.

The deadline is today at 8 pm, so order matters. Build only what the architecture marks
BUILT or SIMULATED. No PvP, no database, no queue, no extras.

Work in these steps, and commit after each one with a clear message:

1. Core: domain.py, events.py, ports.py, rules.py, service.py, bus.py.
2. Adapters and wiring: memory.py, channels.py, simulation.py, bootstrap.py.
3. Demo: __main__.py. It fires the brief's four triggers exactly as written, then
   challenge completed and new follower, then a common item that sends nothing, then one
   event for a player who has disabled the category, then the same event after they enable
   it again. Print each trigger next to what the system did: SENT with the text, or SKIPPED
   with the reason.
4. Tests (unittest), named after the requirement they prove:
   - each of the six event types sends the right text to the right player, including
     Friend Accepted going to user 3 (A14)
   - the three PDF sample texts match word for word (R26 to R28)
   - a disabled category sends nothing and makes no lookup (AD3), and enabled is the
     default (A18)
   - an item below rare, and an unknown item, send nothing (A10, A25)
   - an event with no rule is ignored
   - a failing subscriber does not break the emitter, and a failing channel does not block
     the next one (AD10)
   - two rules on one event class both run (AD9)
5. Docker and scripts: Dockerfile, .dockerignore, .gitignore, .gitattributes, and build,
   run and test scripts as .sh and .cmd. Mark the .sh files executable in git (AD11).
6. README.md at the repo root: what this is, how to build, run and test with Docker, the
   fallback without Docker, the main features, a sample of the demo output, the design in
   a few lines with a link to docs/architecture.md, the main assumptions by ID, the
   dispatch order and why it differs from the brief's sentence (AD3), and how I used AI,
   with a link to docs/prompts/.

Put requirement and decision IDs in comments where they explain why the code is the way
it is. Keep comments short.

Verify before you finish: build the image, run the tests and the demo in Docker, and show
me the real output. If Docker is not running, tell me, run both with local Python instead,
and say plainly that Docker was not verified. Don't say something works unless you ran it.

This machine has Windows Controlled Folder Access on the Documents folder. Create and edit
files with your file tools. If a shell command cannot write inside the repo, that is the
cause: tell me, and don't change any security settings.

Don't push. When you finish, tell me what was built, the test results, and anything left undone.
```
