"""The example usage (R42, R43): python -m notification_system

Each trigger is printed, then fired. The line under it is what the system did:
SENT with the text, printed by the in-app channel, or SKIPPED with the reason,
logged by the service.
"""

from __future__ import annotations

import logging
import sys

from .bootstrap import build_app
from .domain import Category


def show(line: str) -> None:
    print(f"\n>>> {line}")


def main() -> None:
    # The service logs each skip. Print those lines next to the triggers.
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)

    app = build_app()
    # The brief's own names, so its four lines run as written (A8).
    gameEngine = app.game_engine  # noqa: N806
    socialSystem = app.social_system  # noqa: N806
    preferences = app.preferences

    print("Real-time notification system: example usage")
    print("Players: 1 Aria, 2 Borin, 3 Cyra. Every category is on by default (A18).")

    print("\n--- The brief's four example triggers (R44) ---")
    show('gameEngine.playerLeveledUp(1, 15)  # User 1 leveled up to 15')
    gameEngine.playerLeveledUp(1, 15)  # User 1 leveled up to 15

    show('gameEngine.itemAcquired(2, "SwordOfAzeroth")  # User 2 acquired an item')
    gameEngine.itemAcquired(2, "SwordOfAzeroth")  # User 2 acquired an item

    show('socialSystem.friendRequestSent(3, 1)  # User 3 sent a friend request to user 1')
    socialSystem.friendRequestSent(3, 1)  # User 3 sent a friend request to user 1

    show('socialSystem.friendRequestAccepted(1, 3)  # User 1 accepted friend request from 3')
    socialSystem.friendRequestAccepted(1, 3)  # User 1 accepted friend request from 3

    print("\n--- The two event types the brief gives no trigger for (R18, R23) ---")
    show('gameEngine.challengeCompleted(1, "DragonSlayer")  # User 1 completed a challenge')
    gameEngine.challengeCompleted(1, "DragonSlayer")  # User 1 completed a challenge

    show('socialSystem.followerAdded(2, 1)  # User 2 started following user 1')
    socialSystem.followerAdded(2, 1)  # User 2 started following user 1

    print("\n--- An item that is not rare or valuable sends nothing (R17, A10) ---")
    show('gameEngine.itemAcquired(2, "WoodenShield")  # User 2 acquired a common item')
    gameEngine.itemAcquired(2, "WoodenShield")  # User 2 acquired a common item

    print("\n--- A player switches a category off, then on again (R29) ---")
    show('preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)  # User 1 turns Social Events off')
    preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)  # User 1 turns Social Events off

    show('socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1')
    socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1

    show('preferences.set_enabled(1, Category.SOCIAL_EVENTS, True)  # User 1 turns Social Events on')
    preferences.set_enabled(1, Category.SOCIAL_EVENTS, True)  # User 1 turns Social Events on

    show('socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1')
    socialSystem.friendRequestSent(2, 1)  # User 2 sent a friend request to user 1

    print(f"\nDone. {len(app.in_app.delivered)} notifications were sent.")


if __name__ == "__main__":
    main()
