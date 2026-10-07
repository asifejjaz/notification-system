"""Stand-ins for the parts of the platform that emit events (N5, R37).

They know the event bus and the event classes, and nothing about
notifications (R36).

The method names are camelCase on purpose. They are the brief's own names, so
its example triggers run as written (A8, R44). Python naming is used everywhere
else in the project.
"""

from __future__ import annotations

from .events import (
    ChallengeCompleted,
    FollowerAdded,
    FriendRequestAccepted,
    FriendRequestSent,
    ItemAcquired,
    PlayerLeveledUp,
)
from .ports import EventBus


class GameEngine:
    """Emits game events."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus

    def playerLeveledUp(self, user_id: int, level: int) -> None:  # noqa: N802
        self._bus.publish(PlayerLeveledUp(user_id, level))

    def itemAcquired(self, user_id: int, item_id: str) -> None:  # noqa: N802
        self._bus.publish(ItemAcquired(user_id, item_id))

    def challengeCompleted(self, user_id: int, challenge_id: str) -> None:  # noqa: N802
        # Not in the brief. Proposed in the brief's style (A9).
        self._bus.publish(ChallengeCompleted(user_id, challenge_id))


class SocialSystem:
    """Emits social events. The player who acted is the first argument."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus

    def friendRequestSent(self, sender_id: int, recipient_id: int) -> None:  # noqa: N802
        self._bus.publish(FriendRequestSent(sender_id, recipient_id))

    def friendRequestAccepted(self, accepter_id: int, requester_id: int) -> None:  # noqa: N802
        self._bus.publish(FriendRequestAccepted(accepter_id, requester_id))

    def followerAdded(self, follower_id: int, followed_id: int) -> None:  # noqa: N802
        # Not in the brief. Proposed in the brief's style (A9).
        self._bus.publish(FollowerAdded(follower_id, followed_id))
