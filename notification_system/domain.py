"""Domain types. This module imports nothing from the project."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, IntEnum


class Category(Enum):
    """What a player can switch on or off (R29, A17)."""

    GAME_EVENTS = "Game Events"
    SOCIAL_EVENTS = "Social Events"

    @property
    def label(self) -> str:
        return self.value


class NotificationType(Enum):
    """One type per event type. Each type carries its category (R38, A6, AD8)."""

    LEVEL_UP = ("LEVEL_UP", Category.GAME_EVENTS)
    ITEM_ACQUIRED = ("ITEM_ACQUIRED", Category.GAME_EVENTS)
    CHALLENGE_COMPLETED = ("CHALLENGE_COMPLETED", Category.GAME_EVENTS)
    FRIEND_REQUEST = ("FRIEND_REQUEST", Category.SOCIAL_EVENTS)
    FRIEND_ACCEPTED = ("FRIEND_ACCEPTED", Category.SOCIAL_EVENTS)
    NEW_FOLLOWER = ("NEW_FOLLOWER", Category.SOCIAL_EVENTS)

    def __init__(self, code: str, category: Category) -> None:
        self.code = code
        self.category = category


class Rarity(IntEnum):
    """How rare or valuable an item is, lowest first (A10)."""

    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4

    @property
    def label(self) -> str:
        """The word used in a message, for example "legendary" (R27)."""
        return self.name.lower()


@dataclass(frozen=True)
class Item:
    """A game item (A10, A11). The short name is the display name."""

    id: str
    short_name: str
    description: str
    rarity: Rarity


@dataclass(frozen=True)
class Challenge:
    """A quest or achievement. The two are not told apart (A13)."""

    id: str
    name: str


@dataclass(frozen=True)
class Notification:
    """The message for one player.

    The brief says this class is provided, but none came with it, so this is
    the project's own basic definition (R31, A1).
    """

    recipient_id: int
    type: NotificationType
    message: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def category(self) -> Category:
        return self.type.category
