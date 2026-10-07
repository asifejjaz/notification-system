# Step 02: System architecture

**Goal:** choose an architecture for the notification system that meets the functional requirements and stays extensible and modular, before any code is written.

**Tools:** Claude Code in VS Code with Claude Opus 5.5, in two sessions: a planning session that writes and refines prompts, and a build session that runs them.

## Prompts

| Prompt | Status | Notes |
|---|---|---|
| [v1.1](prompt-v1.1.md) | Not run in the build session | My request to the planning session, in my words. It says what the architecture prompt must cover: entities, interactions, attributes and a database schema. |
| [v1.2](prompt-v1.2.md) | Run | Written by the planning session from v1.1. Run in the build session. |
| [v1.3](prompt-v1.3.md) | Run | My approvals and the planning session's four changes, written up by the planning session and applied by it to `docs/architecture.md`. |

There is no v1.0. I numbered my request v1.1 and the generated prompt v1.2.

## What v1.2 adds to my request

v1.2 keeps everything I asked for in v1.1: the main entities, the interactions between them, their attributes and a database schema. The planning session added:

1. **A link to step 01.** The agent reads `docs/requirements.md` version 1.1 first. Settled items are fixed, and it must name any PROPOSED item it wants to change.
2. **A limit on scope.** Extensibility and modularity come first, but the brief says not to build beyond what is asked (R2) and the deadline is close. Each entity is marked BUILT, SIMULATED or EXTENSION.
3. **Conflicts brought into the open.** I asked for a game, a queue and a database schema. The proposed assumptions say there is no game dimension (A27), one event at a time (A26) and no storage (A23). The agent has to decide each one and explain it.
4. **Decisions with trade-offs.** Two candidate architectures are compared, and each significant choice is recorded with its options and trade-off. The interview asks for exactly this.
5. **Extension scenarios.** For a new event type, category, channel, database or queue, the agent lists what changes and what stays untouched.
6. **Diagrams, open decisions and traceability.** Mermaid diagrams that render on GitHub, a recommendation for each open decision, and a table from requirements to components.
7. **An output file and a stopping point.** The result is saved as `docs/architecture.md`, marked PROPOSED, and the agent stops before code.

## Result of v1.2: version 1.0

- Output: [docs/architecture.md](../../architecture.md) version 1.0, status PROPOSED.
- It chose an event bus with one rule per event type, interfaces with in-memory implementations, and one place that wires everything.
- It kept the game, the queue and the database as extension points and documented the database schema.

## My review, and version 1.1

I asked the planning session to review version 1.0. It judged the design sound, listed eleven decisions that needed my approval, and suggested four changes. I approved all eleven and accepted the four changes. Prompt v1.3 records both:

- **Approved:** no game, queue or database in the build; preferences checked before the `Notification` is created; one rarity scale for items; the brief's trigger names; Python 3.13 in Docker; `unittest` with the standard library only; a console demo plus tests; PvP left out.
- **Changed:** several rules per event type (AD9), failure isolation in the bus and the channels (AD10), scripts that work on a reviewer's machine (AD11), and a plain statement that `game_id` is not built.

Versions 1.0 and 1.1 are separate commits, so the diff between them shows exactly what changed.
