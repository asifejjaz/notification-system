# Requirements analysis: real-time notification system

**Status: PROPOSED (2026-10-01).** Nothing here is confirmed yet. Assumptions A1 to A29 and decisions D1 to D8 are waiting for confirmation, and no design or code should rely on them until this line reads CONFIRMED. Three assumptions are worth raising with the hiring contact first: A1, A3 and A4.

Source: the challenge brief, *Coding Challenge: Real-Time Notification System for a Gaming Platform* (PDF, 3 pages). This is requirements analysis only. It proposes no architecture and chooses nothing.

## How to read this document

- **IDs are permanent.** R is a requirement, A an assumption, D an open decision, N something out of scope. An ID is never renumbered or reused. A removed item keeps its row and is marked DROPPED. Code comments, tests and the README refer to these IDs.
- **Quotes.** Text in curly double quotes is copied word for word from the PDF, with line breaks joined. Straight quotes inside it are the PDF's own, and … marks words left out. Code lines from the PDF are shown as `code`, unchanged.
- **PROPOSED** in front of a trigger or a message means it is not in the PDF and is suggested here.
- **Levels** in section 1 follow the PDF's wording:
  - MUST: an instruction or expectation the PDF does not soften (“must”, “should”, “We will”, or a plain instruction such as “Implement”).
  - RECOMMENDED: the PDF softens it (“(Recommended)”, “We recommend”, “will likely”, “For example”).
  - OPTIONAL: the PDF makes it a choice or a permission (“optional”, “welcome”, “You can”, “You are free to”, “feel free”).

## 1. Requirements

46 requirements: 32 MUST, 7 RECOMMENDED, 7 OPTIONAL. They are numbered in the order the PDF states them.

### Introduction (page 1)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R1 | The whole brief is read before any code is written. | MUST | “Read the challenge carefully before you start writing code.” |
| R2 | Only the required features are built, and nothing extra unless it is needed. | MUST | “Focus only on the required features described below; do not build beyond what is asked if you don't need to.” |
| R3 | The requirements come first. Polish happens only if time is left. | RECOMMENDED | “We recommend you focus on the requirements and do additional polishing if you get extra time” |
| R4 | Extra features are allowed, but only after the required ones are complete. | OPTIONAL | “additional features are welcome if you decide to add them after you completed.” |
| R5 | AI tools are used. | RECOMMENDED | “The use of AI tools is not just allowed, it is recommended.” |
| R6 | The repo shows the process followed to understand the requirements and build the features, not only the final files. | MUST | “We want to see the process you followed to understand the requirements and build the features, not just the final files.” |
| R7 | The product compiles and runs. | MUST | “The resulting product must compile and run.” |
| R8 | The repo provides build scripts, and a fresh clone runs using them. | MUST | “We will clone the repo and run it using the build scripts you provide.” |
| R9 | The project is delivered in a public GitHub repository that I own. | MUST | “The delivery is done by uploading the project into a public GitHub repository you own.” |
| R10 | A `README.md` explains how to run the project and lists its main features. | RECOMMENDED | “(Recommended) add a README.md file on the repo that explains how to run it and the main features you included.” |
| R11 | The deliverable keeps a record of my AI use: the prompts, the process from requirements to working solution, the workflows and patterns, and the tools. | MUST | “Your use of AI: the prompts you used and the process you followed to go from requirements to a working solution. Workflows and patterns used, tools used. Keep that as part of the deliverable.” |
| R12 | I can defend the product in the interview: the architecture patterns and why, the tradeoffs, what adding features would involve, and how the system works. This is an interview expectation. The PDF asks for no file (D8). | MUST | “Defending the resulting product: the architecture patterns you chose and why, the tradeoffs behind them, hypothetical scenarios on what will imply adding features on top of what you built, and general questions about how the system works.” |
| R13 | Questions about the challenge can be sent to the HR contact. | OPTIONAL | “Please feel free to reach out to the provided contacts of the HR representative if you have questions about the challenge.” |

### Scenario (page 1)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R14 | The product is a real-time notification system that keeps players informed about important events in the game world and in their social network. | MUST | “You are developing a real-time notification system for a popular online gaming platform. This platform hosts various multiplayer games, and players need to be kept informed about important events happening in the game world and their social network.” |

### Specific Requirements (page 2)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R15 | Players receive real-time notifications about in-game events. | MUST | “In-Game Events: Players should receive real-time notifications about in-game events, such as:” |
| R16 | Level Up: a player is notified when they reach a new level. | MUST | “Level Up: When a player reaches a new level.” |
| R17 | Item Acquired: a player is notified when they obtain a rare or valuable item. What counts as rare or valuable: A10. | MUST | “Item Acquired: When a player obtains a rare or valuable item.” |
| R18 | Challenge Completed: a player is notified when they complete a challenging quest or achievement. | MUST | “Challenge Completed: When a player completes a challenging quest or achievement.” |
| R19 | PvP: a player is notified when another player attacks or defeats them. Whether to build it: D4. | OPTIONAL | “Player vs. Player (PvP) Events: When a player is attacked or defeated by another player (optional, but good to consider).” |
| R20 | Players receive notifications about social events. | MUST | “Social Events: Players should also receive notifications about social events:” |
| R21 | Friend Request: a player is notified when another player sends them a friend request. | MUST | “Friend Request: When another player sends them a friend request.” |
| R22 | Friend Accepted: a notification is sent when a friend request is accepted. Who receives it: A14. | MUST | “Friend Accepted: When a friend request is accepted.” |
| R23 | New Follower: a player is notified when another player starts following them. | MUST | “New Follower: When another player starts following them.” |
| R24 | In-app is the only notification channel. | MUST | “Multiple Notification Channels: For this simplified coding exercise, focus on in-app notifications.” |
| R25 | Notification text is clear, concise and informative. | MUST | “Notification Content: Notifications should be clear, concise, and informative. For example:” |
| R26 | The Level Up text follows the PDF sample. | RECOMMENDED | “Level Up: "Congratulations! You've reached level 15!"” |
| R27 | The Item Acquired text follows the PDF sample. | RECOMMENDED | “Item Acquired: "You've acquired the legendary Sword of Azeroth!"” |
| R28 | The Friend Request text follows the PDF sample. | RECOMMENDED | “Friend Request: "Player 'X' has sent you a friend request."” |
| R29 | Each user can enable or disable notifications for each category of events. | MUST | “User Preferences (Simplified): For this exercise, assume each user can enable or disable notifications for each category of events (e.g., "Game Events," "Social Events").” |
| R30 | Preferences can be held in a simple dictionary or map. | OPTIONAL | “You can represent these preferences with a simple dictionary or map.” |

### Technical Requirements (page 2)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R31 | The solution uses the `Notification` class the PDF says is provided. It is not attached: A1. | MUST | “Notification Class: You are provided with a Notification class.” |
| R32 | The components needed to handle notifications are designed and implemented. | MUST | “Notification Handling: Design and implement the necessary components to handle notifications.” |
| R33 | Those components cover sending notifications, checking user preferences and interacting with the game and social systems, likely as interfaces, services and classes. | RECOMMENDED | “This will likely involve interfaces, services, and classes to manage the sending of notifications, checking user preferences, and interacting with the game and social systems.” |
| R34 | The code is structured to stay flexible and maintainable as the system grows. | MUST | “Consider how you will structure your code to ensure flexibility and maintainability as the system grows.” |
| R35 | There is a mechanism that receives and processes events from different parts of the game. | MUST | “Event Handling: Implement a mechanism to receive and process events from different parts of the game. This should include:” |
| R36 | Game events and social events, emitted by different parts of the platform, are captured and passed to the notification system. | MUST | “Receiving events: Assume that game events (like player leveling up or acquiring an item) and social events (like friend requests) are emitted by different parts of the game platform. You'll need a way to capture these events and pass them to your notification system.” |
| R37 | Events can be simulated using the PDF's examples. | OPTIONAL | “For this exercise, you can simulate these events using the provided examples below.” |
| R38 | Dispatch, step 1: the notification system determines the type of notification. | MUST | “Dispatching notifications: Your notification system should determine the type of notification” |
| R39 | Dispatch, step 2: it creates the `Notification` object. | MUST | “Your notification system should … create the Notification object” |
| R40 | Dispatch, step 3: it checks the user's preferences. | MUST | “Your notification system should … check user preferences” |
| R41 | Dispatch, step 4: it sends the notification. | MUST | “Your notification system should … send the notification.” |
| R42 | An example usage demonstrates how different parts of the game, or simulated game events, trigger notifications. | MUST | “Example Usage: Demonstrate how different parts of the game (or simulated game events) would trigger notifications.” |
| R43 | The example usage clearly shows how events are triggered and how the notification system responds. | MUST | “The example usage should clearly show how events are triggered and how the notification system responds.” |

### Example Event Triggers (page 3)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R44 | The four example triggers can be simulated in test code. Whether their names and argument order are binding: A8. | OPTIONAL | “You can simulate these event triggers in your test code. Imagine these methods are called by various parts of the game platform:”<br>`gameEngine.playerLeveledUp(1, 15); // User 1 leveled up to 15`<br>`gameEngine.itemAcquired(2, "SwordOfAzeroth"); // User 2 acquired an item`<br>`socialSystem.friendRequestSent(3, 1); // User 3 sent a friend request to user 1`<br>`socialSystem.friendRequestAccepted(1, 3); // User 1 accepted friend request from 3` |

### Important Note (page 3)

| ID | Requirement | Level | Exact PDF quote |
|---|---|---|---|
| R45 | The client that delivers and displays notifications can be mocked or simulated as an external dependency. | OPTIONAL | “You are free to mock or simulate this as an external dependency.” |
| R46 | Effort goes into the core notification logic: receiving events, processing them, checking user preferences and triggering the sending. | MUST | “Focus your efforts on the core notification logic: receiving events, processing them, checking user preferences, and triggering the notification sending process.” |

## 2. Event catalog

One row per event type. The PDF names seven. PvP takes two rows because “attacked or defeated” are two different moments (A15).

| Event | R-ID | Category | Trigger | Recipient | Fires when | Data the message needs, and its source | Message text |
|---|---|---|---|---|---|---|---|
| Level Up | R16, text R26 | Game Events | PDF: `gameEngine.playerLeveledUp(1, 15); // User 1 leveled up to 15` | The player who levelled up (argument 1): **user 1** | Every time a player reaches a new level. No filter. | New level `15`: trigger argument 2.<br>No lookup. | PDF sample: “Congratulations! You've reached level 15!” |
| Item Acquired | R17, text R27 | Game Events | PDF: `gameEngine.itemAcquired(2, "SwordOfAzeroth"); // User 2 acquired an item` | The player who obtained the item (argument 1): **user 2** | Only when the item is rare or valuable (A10). Other items send nothing. | Item id `"SwordOfAzeroth"`: trigger argument 2.<br>Display name "Sword of Azeroth": lookup, item id → name (A11).<br>Rarity "legendary": lookup, item id → rarity (A11). The same rarity decides whether the event fires. | PDF sample: “You've acquired the legendary Sword of Azeroth!” |
| Challenge Completed | R18 | Game Events | **PROPOSED** `gameEngine.challengeCompleted(1, "DragonSlayer"); // User 1 completed a challenge` | The player who completed it (argument 1). No PDF example; user 1 in the proposed trigger. | Every completion the game reports. No extra filter (A13). | Challenge id: trigger argument 2.<br>Challenge name: lookup, challenge id → name. | **PROPOSED** "You've completed the challenge 'Dragon Slayer'!" |
| PvP: Attacked | R19 (optional, D4) | Game Events (A17) | **PROPOSED** `gameEngine.playerAttacked(2, 1); // User 2 attacked user 1` | The player who was attacked (argument 2). No PDF example; user 1 in the proposed trigger. | Every attack the game reports. No throttling (A15). | Attacker id: trigger argument 1.<br>Attacker name: lookup, user id → name (A12). | **PROPOSED** "Player 'X' has attacked you." |
| PvP: Defeated | R19 (optional, D4) | Game Events (A17) | **PROPOSED** `gameEngine.playerDefeated(2, 1); // User 2 defeated user 1` | The player who was defeated (argument 2). No PDF example; user 1 in the proposed trigger. | Every defeat the game reports (A15). | Winner id: trigger argument 1.<br>Winner name: lookup, user id → name (A12). | **PROPOSED** "Player 'X' has defeated you." |
| Friend Request | R21, text R28 | Social Events | PDF: `socialSystem.friendRequestSent(3, 1); // User 3 sent a friend request to user 1` | The player the request was sent to (argument 2): **user 1** | Every friend request. | Sender id `3`: trigger argument 1.<br>Sender name, the X in the sample: lookup, user id → name (A12). | PDF sample: “Player 'X' has sent you a friend request.” |
| Friend Accepted | R22 | Social Events | PDF: `socialSystem.friendRequestAccepted(1, 3); // User 1 accepted friend request from 3` | The player whose request was accepted (argument 2): **user 3** (A14) | Every accepted request. | Accepter id `1`: trigger argument 1.<br>Accepter name: lookup, user id → name (A12). | **PROPOSED** "Player 'X' has accepted your friend request." |
| New Follower | R23 | Social Events | **PROPOSED** `socialSystem.followerAdded(2, 1); // User 2 started following user 1` | The player being followed (argument 2). No PDF example; user 1 in the proposed trigger. | Every new follow. | Follower id: trigger argument 1.<br>Follower name: lookup, user id → name (A12). | **PROPOSED** "Player 'X' has started following you." |

Two things the table shows:

- The recipient is not always the first argument. In the PDF's four triggers it is argument 1 for the two game events and argument 2 for the two social events (for Friend Accepted this rests on A14).
- The proposed triggers follow the PDF's pattern: the player who acted comes first, as in `socialSystem.friendRequestSent(3, 1)`.

## 3. Assumptions

Each row is a gap in the PDF and the simplest way to close it. Confirm or change each one.

### Missing inputs

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A1 | “You are provided with a Notification class.” None is attached. The PDF has no embedded file and no link, and no class file was found alongside it. | The project defines its own minimal `Notification` class, and the README says so. Its fields are settled in the design step. | **Yes.** It is the only input the PDF promises and does not include. A real class would fix the fields, and probably the language too (A3, D1). |
| A2 | “the provided contacts of the HR representative” are not in the PDF. | They are in the invitation, not in the PDF. | No. There is nothing to ask. |
| A3 | No language, runtime or stack is named anywhere. | Any mainstream language is acceptable. Which one is D1. | **Yes**, in the same message as A1. The wrong language is the most expensive mistake to make here, and one line settles it. |
| A4 | No deadline, time budget or submission step. The PDF only hints that time is limited (“if you get extra time”) and says where the code goes (R9), not who receives the link. | The deadline is the one in the invitation. The repo link goes to the HR contact. | **Yes**, if the invitation does not already say. A missed deadline cannot be fixed afterwards. |

### Events and dispatch

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A5 | The in-game list opens with “such as”, so it reads as examples. The social list has no such wording. | The seven event types named in the PDF are the complete set (section 2). No others are built. | No. R2 already says to build only what is asked. |
| A6 | The PDF says to “determine the type of notification” but never defines a type. | One notification type per event in section 2. Each type belongs to exactly one category (A17). | No. It is a naming matter inside the solution. |
| A7 | The dispatch sentence lists four steps: “determine the type of notification, create the Notification object, check user preferences, and send the notification”. It creates the object before checking preferences, and the PDF does not say whether that order is binding. | The steps run in the order written. | No. Following the written order cannot be wrong. |
| A8 | `gameEngine` and `socialSystem` are explained only by “Imagine these methods are called by various parts of the game platform”. The PDF does not say whether they are mine to write, or whether their method names and argument order are binding. | They are simulated stand-ins for the platform's own systems (N5), written for this project. The PDF's object names, method names and argument order are kept exactly, apart from letter case if the chosen language's conventions require it (D1). | No. Keeping them as written is the safe reading. |
| A9 | Three event types have no example trigger (Challenge Completed, New Follower, PvP). Four have no sample text (Challenge Completed, Friend Accepted, New Follower, PvP). | The missing triggers and texts are written in the shape and style of the PDF's own. Each is marked PROPOSED in section 2. | No. The PDF leaves them open. |
| A10 | “rare or valuable item”: the trigger carries only a user id and an item id, and its comment says just “User 2 acquired an item”. The PDF does not define rare or valuable, and does not say whether the game or the notification system decides. | The notification system decides. It looks up the item's rarity and notifies only for rare items and better. Other items send nothing. Valuable is not a separate attribute: it is treated as high rarity. | No. Any consistent rule satisfies the brief, and the README states the rule. |
| A11 | The sample text says “the legendary Sword of Azeroth”, but the trigger passes only `"SwordOfAzeroth"`: no display name and no rarity. | A small simulated item catalog maps item id to display name and rarity. This is one reading of “interacting with the game and social systems”. | No. Simulating a lookup is in line with R37. |
| A12 | The sample text says “Player 'X'”, but the triggers carry numeric user ids. The PDF does not say whether X is a name or the id. | X is the player's display name, looked up by user id in a small simulated player directory. | No. The sample reads as a name, and the README states it. |
| A13 | “completes a challenging quest or achievement”: it is unclear whether challenging is a filter in the way rare or valuable is, and whether quests and achievements are separate events. | No filter. The game reports only completions that count, and each one sends a notification. Quests and achievements are one event type. | No. Low stakes, and the README states it. |
| A14 | “Friend Accepted: When a friend request is accepted.” does not say who is notified. The trigger comment reads “User 1 accepted friend request from 3”. | Only the player who sent the request is notified (user 3). The player who accepted it (user 1) is not, because they did it themselves. | No. It is the natural reading, and the README states it. |
| A15 | PvP: “attacked or defeated by another player” could be one event type or two, and a single fight can contain many attacks. The PDF gives no trigger, text or frequency. | Two event types, attacked and defeated. The player on the receiving end is notified once per reported event, with no throttling. This applies only if D4 says to build PvP. | No. The PDF marks PvP optional. |

### Message content

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A16 | The three sample texts follow “For example:”, so it is unclear whether their wording is binding. No language is named for the messages. | The three sample texts are used word for word. Only the level, the item and the player name change. Messages are in English only. | No. Using the PDF's own wording cannot be wrong. |

### Preferences

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A17 | Categories are given as “(e.g., "Game Events," "Social Events")”. The “e.g.” leaves the set open, the event list calls the first group “In-Game Events”, and PvP's category is not stated. | Exactly two categories, named as in the preferences sentence: Game Events and Social Events. In-Game Events and Game Events are the same category. PvP belongs to it, because the PDF lists PvP under In-Game Events. | No. The PDF's two examples are enough. |
| A18 | The PDF does not say what applies to a user who has set no preference. | Every category is enabled by default. A user receives a category unless they have disabled it. | No. Enabled by default is the usual choice, and the README states it. |
| A19 | “each user can enable or disable”: the PDF does not say how or when a preference is changed. | Preferences are set in code, per user and per category, so the example usage and the tests can show an enabled case and a disabled case. No settings screen and no storage (N6). | No. The PDF itself calls preferences simplified. |
| A20 | The PDF does not say what happens to a notification that a preference blocks. | It is dropped: not sent, not stored, and not sent later if the preference changes. | No. That is the plain meaning of disabling a category. |

### Delivery and runtime

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A21 | “real-time” is never defined: no latency figure and no transport. The sentence about social events leaves the word out. | A notification is sent as soon as its event is processed, with no batching, scheduling or polling. The same holds for social events. There is no latency target. | No. Delivery to the client is assumed to exist (N2). |
| A22 | The heading says “Multiple Notification Channels”, but the text under it says to “focus on in-app notifications”. | Only the in-app channel is built (R24, N3). | No. The text is explicit. Adding a channel is a likely interview question (R12). |
| A23 | Nothing is said about keeping notifications: history, an inbox, read or unread state, surviving a restart. | None of it. Everything lives in memory for the length of one run. | No. R2 applies. |
| A24 | Nothing is said about delivery failing, retries, ordering or duplicates. | The simulated delivery client always succeeds. There are no retries and no de-duplication, and notifications go out in the order their events arrive. | No. Delivery is assumed to exist and can be mocked (N2, R45). |
| A25 | Nothing is said about bad input: unknown user or item ids, a player sending a request to themselves, the same event arriving twice. | The systems that emit events are trusted, so events are not validated or de-duplicated. An unknown item sends nothing, because it cannot be shown to be rare. A player with no known name is shown by id. | No. The README states the behaviour. |
| A26 | Nothing is said about load, concurrency or performance, although the platform is “popular” and the code should hold up “as the system grows”. | One process, one event at a time, no performance targets. | No. A likely interview topic (R12), but nothing to build. |
| A27 | “This platform hosts various multiplayer games”: the PDF does not say whether an event or a notification belongs to a particular game. | There is no game dimension. Events form one stream for the whole platform, and messages do not name a game. | No. None of the example triggers carries a game. |

### Process

| ID | Gap | Simplest assumption | Worth asking the hiring contact? |
|---|---|---|---|
| A28 | Tests are mentioned (“(for testing)”, “your test code”) but never required. | The repo includes a small automated test suite that uses the four PDF triggers. | No. The PDF mentions test code twice, and tests back up R7. |
| A29 | “build scripts” and “run it” are not specified: which commands, on which operating system, and what a run should show. | One command builds and one command runs, from a fresh clone, on Windows, macOS and Linux. A run shows the example usage (R42). The README lists the prerequisites. | No. Covering all three systems costs less than asking. |

## 4. Open decisions

Choices the PDF leaves open. Nothing is chosen here.

| ID | Decision | Options | Hints in the PDF |
|---|---|---|---|
| D1 | Language and runtime, including the version to target. | Any language with classes, interfaces and a map type. For example Java, C#, TypeScript on Node.js, Kotlin, Python or Go. | The PDF names no language (A3).<br>The example triggers use C-style syntax: camelCase method calls, semicolons, `//` comments and double-quoted strings. They are valid as written in Java, C#, JavaScript and TypeScript. camelCase method names are the convention in Java and in JavaScript or TypeScript, and not in C#.<br>“must compile and run” suggests a compiled or type-checked language but does not require one.<br>“Notification class” and “interfaces, services, and classes” suggest an object-oriented style.<br>“dictionary or map” uses both common names for the same structure, so it favours no language.<br>A real `Notification` class, if one exists, would probably settle this (A1). |
| D2 | Build and run scripts. | (a) The chosen language's own tooling, called directly, for example npm scripts, a Maven or Gradle wrapper, or the `dotnet` CLI.<br>(b) Wrapper scripts on top, one set per operating system: `build.sh` and `run.sh`, plus `.ps1` or `.cmd` files.<br>(c) A Makefile.<br>(d) Docker, so a reviewer needs nothing else installed. | “We will clone the repo and run it using the build scripts you provide.” The word scripts is plural, and the reviewers' operating system is not stated (A29).<br>The README “explains how to run it” (R10). |
| D3 | Test framework, and whether the tests run as part of the build. | Depends on D1. For example JUnit for Java, xUnit or NUnit for C#, Jest, Vitest or the built-in Node.js test runner for TypeScript, pytest for Python, the built-in `testing` package for Go. | “Example Event Triggers (for testing)”<br>“You can simulate these event triggers in your test code.”<br>No framework is named, and tests are not strictly required (A28). |
| D4 | Whether to build the optional PvP events (R19). | (a) Leave them out and say so in the README.<br>(b) Add them after every MUST is done.<br>(c) Build them from the start. | “(optional, but good to consider)”<br>“do not build beyond what is asked if you don't need to”<br>“additional features are welcome if you decide to add them after you completed” |
| D5 | The form of the example usage (R42, R43). | (a) A console demo that fires the triggers and prints what was sent and what was skipped.<br>(b) The test suite as the demonstration.<br>(c) Both.<br>(d) A sample run copied into the README, on top of any of the above. | “The example usage should clearly show how events are triggered and how the notification system responds.”<br>“You can simulate these event triggers in your test code.” |
| D6 | Third-party dependencies. | (a) The standard library only, plus the test framework.<br>(b) Libraries allowed, for example for events or dependency injection. | No direct hint.<br>“We will clone the repo and run it using the build scripts you provide.” Every dependency is one more thing that has to install on a reviewer's machine. |
| D7 | Format and depth of the AI-use record (R6, R11). | (a) The prompts word for word, one file per step, as already started in `docs/prompts/`.<br>(b) The prompts plus a short note on each result and what I changed.<br>(c) Full exported transcripts.<br>Separately: where the workflows, patterns and tools are written up (a README section or a file of their own), and whether the commit history should show the steps, with one commit per step. | “the prompts you used and the process you followed to go from requirements to a working solution. Workflows and patterns used, tools used. Keep that as part of the deliverable.”<br>“not just the final files” |
| D8 | Whether to write down the design decisions I will have to defend (R12). | (a) Nothing written; answer from memory.<br>(b) A short decisions and tradeoffs section in the README.<br>(c) A separate decisions file. | “the architecture patterns you chose and why, the tradeoffs behind them, hypothetical scenarios on what will imply adding features on top of what you built”<br>The PDF asks for this in the interview, not in writing. |

## 5. Out of scope

Stated means the PDF says it directly. Implied means the PDF tells me to assume or simplify it, which leaves nothing to build.

| ID | Not building | Stated or implied | PDF quote |
|---|---|---|---|
| N1 | Showing the notification in the game client, or any other user interface. | Stated | “The actual display of the notification in the game client is not part of this exercise's scope.” |
| N2 | The client or mechanism that finally delivers the notification to the player, including the game client's real-time receiving side. It can be mocked (R45). | Stated | “You can assume that there is an existing notification client or mechanism to handle the final delivery and display of the notification.”<br>“Assume the game client has a mechanism to receive these notifications in real-time.” |
| N3 | Any channel other than in-app, such as push notifications or email. | Stated | “For this simplified coding exercise, focus on in-app notifications.”<br>“(In a real-world scenario, you'd have push notifications, email, etc., but we're simplifying for the interview.)” |
| N4 | Features beyond the required ones, at least until the required ones are complete (R4). | Stated | “Focus only on the required features described below; do not build beyond what is asked if you don't need to.” |
| N5 | A real game engine or social system. The sources of events are assumed to exist and are simulated. | Implied | “Assume that game events (like player leveling up or acquiring an item) and social events (like friend requests) are emitted by different parts of the game platform.”<br>“For this exercise, you can simulate these events using the provided examples below.” |
| N6 | A full preferences feature: storage, a settings screen, or anything finer than on or off per category. | Implied | “User Preferences (Simplified): For this exercise, assume each user can enable or disable notifications for each category of events”<br>“You can represent these preferences with a simple dictionary or map.” |

## 6. Coverage check

Every line on the three pages was checked against sections 1 to 5. **Result: no line that sets an expectation is left without an ID.**

Lines that set or shape an expectation but are not quoted in section 1, and where they are covered:

| PDF text | Covered by |
|---|---|
| “Coding Challenge: Real-Time Notification System for a Gaming Platform” (the title; the expectation is in the words Real-Time) | R14, A21 |
| “This is what we are expecting:” | Introduces R7 to R10 |
| “The follow up interview will have two parts:” | Introduces R11 and R12 |
| “Assume the game client has a mechanism to receive these notifications in real-time.” | N2, A21 |
| “(In a real-world scenario, you'd have push notifications, email, etc., but we're simplifying for the interview.)” | N3 |
| “Example Event Triggers (for testing)” (a heading) | R44, A28, D3 |
| “The actual display of the notification in the game client is not part of this exercise's scope.” | N1 |
| “You can assume that there is an existing notification client or mechanism to handle the final delivery and display of the notification.” | N2 |

Lines that set no expectation and so have no ID: the subtitle under the title, the other section headings, the header and footer on each page, and “Have fun with it.”
