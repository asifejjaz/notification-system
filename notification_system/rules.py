"""One rule per event type (AD4).

A rule holds everything specific to its event type: the notification type, who
receives it, whether the event qualifies, and the text. Adding an event type
means adding a rule here and one line in default_rules(). The service does not
change.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .domain import Notification, NotificationType, Rarity
from .events import (
    ChallengeCompleted,
    Event,
    FollowerAdded,
    FriendRequestAccepted,
    FriendRequestSent,
    ItemAcquired,
    PlayerLeveledUp,
)
from .ports import ChallengeCatalog, ItemCatalog, PlayerDirectory


class NotificationRule(ABC):
    """Turns one event class into a notification."""

    event_type: type[Event]
    notification_type: NotificationType  # R38: the rule fixes the type

    @abstractmethod
    def recipient_id(self, event: Event) -> int:
        """The player to notify. Needs no lookup (AD3)."""

    @abstractmethod
    def create(self, event: Event) -> Optional[Notification]:
        """The notification (R39), or None if the event does not qualify."""

    def _notification(self, event: Event, message: str) -> Notification:
        return Notification(self.recipient_id(event), self.notification_type, message)


class LevelUpRule(NotificationRule):
    """R16. Every new level notifies the player who reached it."""

    event_type = PlayerLeveledUp
    notification_type = NotificationType.LEVEL_UP

    def recipient_id(self, event: PlayerLeveledUp) -> int:
        return event.user_id

    def create(self, event: PlayerLeveledUp) -> Optional[Notification]:
        # R26: the brief's sample text, word for word (A16).
        return self._notification(event, f"Congratulations! You've reached level {event.level}!")


class ItemAcquiredRule(NotificationRule):
    """R17. Only a rare or valuable item notifies the player who got it."""

    event_type = ItemAcquired
    notification_type = NotificationType.ITEM_ACQUIRED
    notify_from = Rarity.RARE  # A10: what counts as rare or valuable

    def __init__(self, items: ItemCatalog) -> None:
        self._items = items

    def recipient_id(self, event: ItemAcquired) -> int:
        return event.user_id

    def create(self, event: ItemAcquired) -> Optional[Notification]:
        item = self._items.get(event.item_id)
        # A10, A25: an item below RARE sends nothing, and neither does an
        # unknown item, because it cannot be shown to be rare.
        if item is None or item.rarity < self.notify_from:
            return None
        # R27: the brief's sample text. The trigger carries only the item id,
        # so the rarity word and the name come from the catalog (A11).
        return self._notification(event, f"You've acquired the {item.rarity.label} {item.short_name}!")


class ChallengeCompletedRule(NotificationRule):
    """R18. Every completion the game reports notifies the player (A13)."""

    event_type = ChallengeCompleted
    notification_type = NotificationType.CHALLENGE_COMPLETED

    def __init__(self, challenges: ChallengeCatalog) -> None:
        self._challenges = challenges

    def recipient_id(self, event: ChallengeCompleted) -> int:
        return event.user_id

    def create(self, event: ChallengeCompleted) -> Optional[Notification]:
        challenge = self._challenges.get(event.challenge_id)
        # An unknown challenge is shown by its id, as A25 does for players.
        name = challenge.name if challenge else event.challenge_id
        return self._notification(event, f"You've completed the challenge '{name}'!")


class FriendRequestRule(NotificationRule):
    """R21. Notifies the player the request was sent to."""

    event_type = FriendRequestSent
    notification_type = NotificationType.FRIEND_REQUEST

    def __init__(self, players: PlayerDirectory) -> None:
        self._players = players

    def recipient_id(self, event: FriendRequestSent) -> int:
        return event.recipient_id

    def create(self, event: FriendRequestSent) -> Optional[Notification]:
        # R28: the brief's sample text. X is the sender's display name (A12).
        sender = self._players.display_name(event.sender_id)
        return self._notification(event, f"Player '{sender}' has sent you a friend request.")


class FriendAcceptedRule(NotificationRule):
    """R22. Notifies the player whose request was accepted, not the accepter (A14)."""

    event_type = FriendRequestAccepted
    notification_type = NotificationType.FRIEND_ACCEPTED

    def __init__(self, players: PlayerDirectory) -> None:
        self._players = players

    def recipient_id(self, event: FriendRequestAccepted) -> int:
        return event.requester_id

    def create(self, event: FriendRequestAccepted) -> Optional[Notification]:
        accepter = self._players.display_name(event.accepter_id)
        return self._notification(event, f"Player '{accepter}' has accepted your friend request.")


class NewFollowerRule(NotificationRule):
    """R23. Notifies the player who gained the follower."""

    event_type = FollowerAdded
    notification_type = NotificationType.NEW_FOLLOWER

    def __init__(self, players: PlayerDirectory) -> None:
        self._players = players

    def recipient_id(self, event: FollowerAdded) -> int:
        return event.followed_id

    def create(self, event: FollowerAdded) -> Optional[Notification]:
        follower = self._players.display_name(event.follower_id)
        return self._notification(event, f"Player '{follower}' has started following you.")


def default_rules(
    players: PlayerDirectory, items: ItemCatalog, challenges: ChallengeCatalog
) -> list[NotificationRule]:
    """Every rule the system runs. A new event type adds one line here."""
    return [
        LevelUpRule(),
        ItemAcquiredRule(items),
        ChallengeCompletedRule(challenges),
        FriendRequestRule(players),
        FriendAcceptedRule(players),
        NewFollowerRule(players),
    ]
