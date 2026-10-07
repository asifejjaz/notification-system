# Step 01: Requirements analysis

**Goal:** turn the challenge brief into numbered requirements, assumptions and open decisions before any design or code.

**Tools:** Claude Code in VS Code with Claude Opus 5.5, in two sessions:

- a planning session, where I review and refine each prompt before it runs
- a build session, which runs the prompts in this repo

## Prompts

| Prompt | Status | Notes |
|---|---|---|
| [v1](prompt-v1.md) | Not run | My first draft. |
| [v2](prompt-v2.md) | Run | Rewritten by the planning session after it reviewed v1 against the brief. Run as written. |
| [v3](prompt-v3.md) | Run | My own decisions after reviewing the proposed requirements, in my words. Run in the planning session, which applied them to `docs/requirements.md`. |

## What changed in v2, and why

I asked the planning session whether v1 was good enough to extract the requirements and assumptions. It kept what worked in v1: stable IDs, a PDF quote behind every requirement, and the question about anything "provided" but not attached. It found six gaps, and v2 closes them:

1. **Requirements outside the feature list.** The build scripts, the README and the record of my AI use are in the brief's introduction, so v1 could miss them. v2 asks for them by name.
2. **Decisions the brief leaves open.** The brief names no language, and the product must compile and run, so that choice has to come first. v2 asks for a list of open decisions (D1, D2, ...) without choosing.
3. **Events with no example.** v1 asked only about the four example triggers and the three sample texts. v2 asks for one event catalog covering every event type, with missing triggers and texts marked PROPOSED.
4. **Tags that match the brief.** v1 used MUST, OPTIONAL and OUT-OF-SCOPE. The brief calls the README "recommended", so v2 uses MUST, RECOMMENDED and OPTIONAL, and gives out-of-scope items their own list.
5. **The hiring contact.** The brief invites questions, so v2 asks which assumptions are worth raising.
6. **An output file and a stopping point.** v2 saves the result to a file that can be committed, and stops before design.

v2 also adds a coverage check: every sentence in the brief that sets an expectation must map to an ID.

## Result of v2: version 1.0

- Output: [docs/requirements.md](../../requirements.md) version 1.0, status PROPOSED. It has 46 requirements, 29 assumptions, 8 open decisions and 6 out-of-scope items.
- The result came from the v2 prompt alone. I sent no follow-up messages.
- Three assumptions were flagged as worth raising with the hiring contact: A1 (the `Notification` class is not attached), A3 (no language is named) and A4 (no deadline or submission step).

## My review, and version 1.1

I asked the planning session to review version 1.0. It checked every quote against the brief, found no errors and suggested six revisions. Prompt v3 is my own list of decisions after that review. It settles seven assumptions:

- **A1:** assume a basic `Notification` class.
- **A2:** the HR contact is the email address that sent me the challenge.
- **A3:** Python, run in Docker, with Docker as the only prerequisite. This also decides D1 and D2 and changes A29.
- **A4:** the deadline is 7 October 2026 at 8 pm.
- **A7:** the brief's dispatch order is binding unless a better design is suggested. The planning session suggested checking preferences before creating the `Notification` object. That is PROPOSED for the design step.
- **A10:** an `Item` class carries an attribute for how rare, valuable or important the item is.
- **A11:** each item has a short name and a description.

Versions 1.0 and 1.1 are separate commits, so the diff between them shows exactly what I changed. Every assumption and decision that version 1.1 does not mark is still PROPOSED.
