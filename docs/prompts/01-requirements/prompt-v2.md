# Step 01: Requirements analysis (prompt v2)

**Status:** run as written, in Claude Code with Claude Opus 5.5. The [step README](README.md) explains how it differs from v1.

```text
I'm doing a hiring coding challenge. The full brief is in the PDF at
C:\Users\HP\Documents\Career\coding challenge\Coding Challenge.pdf
Read all of it, including the intro, delivery and interview sections, not just the feature list.

This step is requirements analysis only. Don't write code or propose an architecture yet.
Use markdown tables.

1. Requirements (R1, R2, ...): every requirement in the PDF, including delivery and process
   ones such as build scripts, the README and documenting my AI use.
   Columns: ID | requirement | MUST / RECOMMENDED / OPTIONAL | exact PDF quote.
   Every requirement needs a quote. If you can't quote it, it's an assumption, not a requirement.

2. Event catalog: one row per event type in the PDF, including those with no example trigger
   or sample text.
   Columns: event | R-ID | category | trigger (verbatim from the PDF, or proposed and marked
   PROPOSED) | recipient (give the user id for the four example triggers) | fires when
   (e.g. only for rare items) | data the message needs and where it comes from (a trigger
   argument, or a lookup such as item id -> name and rarity) | message text (the PDF sample,
   or proposed and marked PROPOSED).

3. Assumptions (A1, A2, ...): every ambiguity or missing input, including anything the PDF
   says is "provided" but isn't attached.
   Columns: ID | gap | simplest assumption | worth asking the hiring contact? (yes/no and why).

4. Open decisions (D1, D2, ...): choices the PDF leaves to me, such as language and runtime,
   build and run scripts, and test framework. List the options and any hints in the PDF.
   Don't choose yet.

5. Out of scope (N1, N2, ...): what the PDF says not to build, with quotes.

6. Coverage check: any sentence in the PDF that sets an expectation but isn't covered by an
   R, A, D or N item.

IDs are permanent: never renumber, and mark removed items DROPPED. We'll reference them in
code comments, tests and the README.

Save the result as docs/requirements.md in the notification-system repo, marked PROPOSED.
Then stop. I'll confirm or change the assumptions and decisions before we design anything.
```
