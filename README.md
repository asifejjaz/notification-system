# Real-time notification system for a gaming platform

A coding challenge solution. Game and social events are published on an event bus, and a notification service turns each one into an in-app notification for the right player, unless that player has switched the category off.

It is written in Python with the standard library only, and it runs in Docker.

## Run it

Docker is the only prerequisite.

| Step | Linux, macOS, Git Bash | Windows | The command the script runs |
|---|---|---|---|
| Build | `./build.sh` | `build.cmd` | `docker build -t notification-system .` |
| Run the demo | `./run.sh` | `run.cmd` | `docker run --rm notification-system` |
| Run the tests | `./test.sh` | `test.cmd` | `docker run --rm notification-system python -m unittest discover -s tests -v` |

**Without Docker:** on Python 3.10 or later, from the repo root. There is nothing to install.

```sh
python -m notification_system                 # the demo
python -m unittest discover -s tests -v       # the tests
```

Checked on 7 October 2026 with Docker 28.3.2 on Windows: the image builds, the 23 tests pass in the container (Python 3.13) and on local Python 3.11, and the demo prints the output below.

## What it does

- **Six event types become notifications.** Level up, item acquired, challenge completed, friend request, friend accepted and new follower. The three texts the brief gives are used word for word.
- **Each notification goes to the right player.** A friend request goes to the player it was sent to. An accepted request goes to the player who sent it.
- **Players choose what they receive.** Each player can switch Game Events and Social Events on or off. Both are on by default.
- **Only rare or valuable items notify.** A common item, or an item the catalog does not know, sends nothing.
- **Delivery is in-app only.** The game client is simulated: it prints each notification and keeps it so tests can read it.
- **A failure stays contained.** An error in a subscriber never reaches the game or social system that emitted the event, and one failing channel does not block the next.

PvP events are optional in the brief and are not built. The architecture shows what adding them takes: two event classes, two notification types and two rules, with the dispatcher untouched.

## Demo output

This is the real output of `docker run --rm notification-system`. Each `>>>` line is a trigger, and the line under it is what the system did. The first four triggers are the brief's own.

```text
Real-time notification system: example usage
Players: 1 Aria, 2 Borin, 3 Cyra. Every category is on by default (A18).

--- The brief's four example triggers (R44) ---

>>> gameEngine.playerLeveledUp(1, 15)  # User 1 leveled up to 15
SENT    in-app to user 1: Congratulations! You've reached level 15!

>>> gameEngine.itemAcquired(2, "SwordOfAzeroth")  # User 2 acquired an item
SENT    in-app to user 2: You've acquired the legendary Sword of Azeroth!

>>> socialSystem.friendRequestSent(3, 1)  # User 3 sent a friend request to user 1
SENT    in-app to user 1: Player 'Cyra' has sent you a friend request.

>>> socialSystem.friendRequestAccepted(1, 3)  # User 1 accepted friend request from 3
SENT    in-app to user 3: Player 'Aria' has accepted your friend request.

--- The two event types the brief gives no trigger for (R18, R23) ---

>>> gameEngine.challengeCompleted(1, "DragonSlayer")  # User 1 completed a challenge
SENT    in-app to user 1: You've completed the challenge 'Dragon Slayer'!

>>> socialSystem.followerAdded(2, 1)  # User 2 started following user 1
SENT    in-app to user 1: Player 'Borin' has started following you.

--- An item that is not rare or valuable sends nothing (R17, A10) ---

>>> gameEngine.itemAcquired(2, "WoodenShield")  # User 2 acquired a common item
SKIPPED ITEM_ACQUIRED for user 2: the event does not qualify

--- A player switches a category off, then on again (R29) ---

>>> preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)  # User 1 turns Social Events off

>>> socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1
SKIPPED FRIEND_REQUEST for user 1: 'Social Events' is disabled

>>> preferences.set_enabled(1, Category.SOCIAL_EVENTS, True)  # User 1 turns Social Events on

>>> socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1
SENT    in-app to user 1: Player 'Borin' has sent you a friend request.

Done. 7 notifications were sent.
```

## The design in a few lines

The system is event-driven and runs in one process.

1. `GameEngine` and `SocialSystem` are simulated. Each trigger becomes an event object, published on an event bus. They know nothing about notifications.
2. `NotificationService` subscribes to the bus. It finds the rule registered for the event's class. The rule fixes the notification type, and the type fixes the category.
3. The service checks the recipient's preference for that category.
4. The rule creates the `Notification`, looking up player names and items through interfaces.
5. The service sends it on every configured channel. Today that is one: the simulated in-app channel.

Everything specific to one event type lives in one rule class. Adding an event type means one event class, one enum member, one rule and one line that registers it. The service, the bus, the stores and the channel do not change.

| File | What it holds |
|---|---|
| `notification_system/domain.py`, `events.py` | `Notification`, the types and categories, `Item`, and the six event classes |
| `notification_system/ports.py` | The six interfaces the core depends on |
| `notification_system/rules.py` | One rule per event type |
| `notification_system/service.py` | The dispatcher |
| `notification_system/bus.py`, `memory.py`, `channels.py` | The in-process bus, the in-memory stores, the in-app channel |
| `notification_system/simulation.py` | `GameEngine` and `SocialSystem` |
| `notification_system/bootstrap.py` | The only place that wires things together |
| `notification_system/__main__.py` | The demo |
| `tests/` | 23 tests, each named after the requirement or decision it proves |

The full design is in [docs/architecture.md](docs/architecture.md): the eleven decisions with their trade-offs (AD1 to AD11), the entities, a sequence diagram, the database schema the in-memory stores would map to, and what each kind of extension would change.

## Dispatch order, and why it differs from the brief

The brief says the system should “determine the type of notification, create the Notification object, check user preferences, and send the notification”.

This system checks preferences **before** it creates the `Notification`: type, check, create, send. All four steps still happen (decision AD3).

The check needs only the recipient and the category, and both are known as soon as the rule is found. So a notification the player has switched off costs no lookup and no object. That matters once the lookups for names and items are calls to other services. A test proves that a blocked notification makes no lookup.

Going back to the brief's order means moving one block in `NotificationService._dispatch`.

## Main assumptions

The brief leaves gaps. [docs/requirements.md](docs/requirements.md) lists every requirement with its quote (R1 to R46) and every assumption (A1 to A29). These are the ones that shape what you see:

| ID | Assumption |
|---|---|
| A1 | The brief says a `Notification` class is provided, but none came with it. The project defines its own. |
| A8 | `GameEngine` and `SocialSystem` keep the brief's camelCase method names, so its example lines run as written. Python naming is used everywhere else. |
| A10, A11 | An item has a rarity, from common to legendary. Items notify from rare up. The trigger carries only an item id, so the name and the word "legendary" come from a simulated item catalog. |
| A12 | "Player 'X'" is the player's display name, looked up by id in a simulated player directory. A player with no known name is shown by id (A25). |
| A14 | Friend Accepted notifies the player who sent the request, not the one who accepted it. |
| A17 | There are two categories: Game Events and Social Events. |
| A18 | Every category is on until a player switches it off. |
| A20 | A notification blocked by a preference is dropped. It is not stored or sent later. |
| A21 | Real-time means the notification is sent as soon as the event is processed, in the same call. There is no queue, batch or polling. |
| A23 | Nothing is stored. Everything lives in memory for one run. |

## How I used AI

I used Claude Code in VS Code with Claude Opus 5.5, in two sessions: a planning session that wrote and reviewed prompts with me, and a build session that ran them. The work went in three steps, and each step stopped for my review before the next one began.

| Step | What the AI produced | What I decided |
|---|---|---|
| [01 Requirements](docs/prompts/01-requirements/) | Every requirement with its quote from the brief, the assumptions, the open decisions and what is out of scope | The language, Docker, the deadline, the `Notification` class and how items are modelled |
| [02 Architecture](docs/prompts/02-architecture/) | Two candidate designs, the decisions with trade-offs, the entities, the diagrams and the extension scenarios | I approved the design and accepted four changes from the review, including failure isolation and several rules per event |
| [03 Implementation](docs/prompts/03-implementation/) | The code, the tests, the Docker setup and this README, built from the confirmed design in a fixed order, with one commit per part | Nothing is pushed until I have checked the result |

The patterns I relied on:

- **Prompts are files.** Every prompt is in [docs/prompts/](docs/prompts/), word for word, with a README per step that says what changed between versions and why.
- **Documents before code.** The AI proposed, I reviewed, and only confirmed versions were built from. The proposed and confirmed versions are separate commits, so the diff shows what I changed.
- **IDs carry through.** Requirement and decision IDs from the documents appear in code comments and test names, so any line can be traced back to the brief.
- **Proof, not claims.** The build prompt required the tests and the demo to be run in Docker and the real output shown.
