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

## What changed in v2, and why

I asked the planning session whether v1 was good enough to extract the requirements and assumptions. It kept what worked in v1: stable IDs, a PDF quote behind every requirement, and the question about anything "provided" but not attached. It found six gaps, and v2 closes them:

1. **Requirements outside the feature list.** The build scripts, the README and the record of my AI use are in the brief's introduction, so v1 could miss them. v2 asks for them by name.
2. **Decisions the brief leaves open.** The brief names no language, and the product must compile and run, so that choice has to come first. v2 asks for a list of open decisions (D1, D2, ...) without choosing.
3. **Events with no example.** v1 asked only about the four example triggers and the three sample texts. v2 asks for one event catalog covering every event type, with missing triggers and texts marked PROPOSED.
4. **Tags that match the brief.** v1 used MUST, OPTIONAL and OUT-OF-SCOPE. The brief calls the README "recommended", so v2 uses MUST, RECOMMENDED and OPTIONAL, and gives out-of-scope items their own list.
5. **The hiring contact.** The brief invites questions, so v2 asks which assumptions are worth raising.
6. **An output file and a stopping point.** v2 saves the result to a file that can be committed, and stops before design.

v2 also adds a coverage check: every sentence in the brief that sets an expectation must map to an ID.
