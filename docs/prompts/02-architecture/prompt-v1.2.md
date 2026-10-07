# Step 02: System architecture (prompt v1.2)

**Status:** written by the planning session from [prompt v1.1](prompt-v1.1.md). Not run yet. The [step README](README.md) explains what it adds.

```text
This is step 02: system architecture. Step 01, requirements analysis, is done.

Before anything else, read docs/requirements.md (version 1.1) in the notification-system
repo, and the brief at C:\Users\HP\Documents\Career\coding challenge\Coding Challenge.pdf
Items marked CONFIRMED, CHANGED or DECIDED are fixed. Items still PROPOSED are defaults:
if your design needs to change one, say so by ID and give the reason. Don't override it silently.

Design the architecture for the notification system. Don't write code yet.

What matters most: the brief asks for code that stays flexible and maintainable as the
system grows (R34), and the interview will ask what it takes to add features (R12). So
extensibility and modularity come first. R2 still applies: don't design more than the
requirements need. The deadline in A4 is today, so the part that gets built must be small.
Design the seams for everything else and mark it as an extension, not as work to build.

Produce these sections:

1. Summary: the architecture in ten lines or fewer, and the patterns it uses.

2. Quality goals: the non-functional requirements you take from the brief (extensibility,
   modularity, maintainability, testability, real-time delivery, simplicity), in priority
   order. For each: the requirement ID or quote behind it, and how the design meets it.

3. Options: two candidate architectures compared in a short table, and the one you choose
   with the reason. Record each significant choice as an architecture decision
   (AD1, AD2, ...): options, choice, why, trade-off. Include the dispatch order from A7.

4. Entities: every main entity. Consider at least player, game, game engine, social system,
   event, notification, notification type, category, user preferences, item, challenge,
   delivery channel and queue. For each: its purpose, main attributes with types, its
   relationships, and its status: BUILT, SIMULATED or EXTENSION. If an entity conflicts
   with an assumption (for example game with A27, or queue with A26), decide and explain.

5. Interactions: the actions and events between entities, as a table (who, does what,
   to whom, what happens next). Add a Mermaid sequence diagram for
   socialSystem.friendRequestSent(3, 1), showing the path where the notification is sent
   and the path where the recipient has disabled the category.

6. Data model: a database schema for the entities that would be stored (tables, columns,
   types, keys, relationships), with a Mermaid ER diagram. State whether the build uses a
   database or in-memory stores behind an interface (A23), and how the two map.

7. Modules: the Python package layout, the interfaces between modules, and which way
   dependencies point. Add a Mermaid component diagram.

8. Extension scenarios: for each of these, list exactly which files or classes change and
   which stay untouched: a new event type, a new category, a new channel such as email or
   push, PvP events (D4), a real database, a message queue, and many instances at once.

9. Open decisions: recommend an answer for D1 (the Python version), D3, D4, D5, D6 and D8,
   and for whether trigger names keep the brief's camelCase or follow Python naming (A8).
   One line of reasoning each. I will confirm them.

10. Traceability: a table mapping each MUST requirement from R14 to R46 to the component
    that satisfies it.

Keep it short enough to read in ten minutes: tables and diagrams over prose.
Use the existing IDs, and never renumber them.

Save the result as docs/architecture.md, marked PROPOSED, version 1.0. Then stop.
I'll confirm or change the design before any code is written.
```
