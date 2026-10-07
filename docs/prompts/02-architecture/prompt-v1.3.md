# Step 02: System architecture (prompt v1.3)

**Status:** run on 2026-10-07 in the planning session, in Claude Code with Claude Opus 5.5. I asked the planning session to review the proposed architecture, approved its list, and asked it to write this prompt and apply it. The [step README](README.md) has the result.

```text
Update docs/architecture.md from version 1.0 to version 1.1. Don't write code.

I approve the design. Record these approvals and change the status to CONFIRMED:

1.  Game, queue and database: none is built. They stay extension points, and the schema
    in section 6 stays as documentation (A27, A26, A23, AD6).
2.  Dispatch order (A7, AD3): check preferences before creating the Notification.
    The README must state it.
3.  Rare or valuable (A10): one ordered rarity scale from common to legendary.
    Notify from rare upward.
4.  Trigger names (A8): keep the brief's camelCase for the GameEngine and SocialSystem
    methods and for the demo's two variables. Python naming everywhere else.
5.  Python version (D1): 3.13, as the python:3.13-slim image.
6.  Tests and libraries (D3, D6): unittest, standard library only.
7.  Scripts (D2): plain docker build and docker run commands, wrapped in .sh and .cmd files.
8.  PvP (D4): left out, described as an extension.
9.  Example usage (D5): a console demo plus tests.
10. Decisions record (D8): docs/architecture.md is the record, and the README links to it.
11. Notification fields (A1): recipient, type, message and created time.

Then make these four changes. They came from the planning session's review:

A. Several rules per event type. The registry maps an event class to a list of rules, so
   one event can produce more than one notification without changing the service. Add an
   extension scenario for an event that notifies more than one player.
B. Failure isolation. The bus catches and logs a subscriber's error, so a notification
   failure never breaks the emitter. The service catches and logs a failure per channel,
   so one channel cannot block another.
C. Scripts that work on a reviewer's machine. A .gitattributes that keeps .sh files on
   Unix line endings, .sh files marked executable in git, and a documented fallback
   without Docker: python -m notification_system on Python 3.10 or later.
D. Game: say plainly that no game_id field is built.

Record A, B and C as new architecture decisions (AD9, AD10, AD11). Keep every existing ID.
Add a version history table.
```
