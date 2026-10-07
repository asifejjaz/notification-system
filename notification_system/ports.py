"""The interfaces the core depends on (R33, AD5).

Every implementation lives outside the core and is chosen in bootstrap.py, so
a database, a queue or a real client can replace one without touching the core.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, Optional

from .domain import Category, Challenge, Item, Notification
from .events import Event

Subscriber = Callable[[Event], None]


class EventBus(ABC):
    """Carries events from the parts that emit them to subscribers (R35, R36)."""

    @abstractmethod
    def subscribe(self, event_type: type[Event], subscriber: Subscriber) -> None:
        """Call subscriber for every published event of exactly this class."""

    @abstractmethod
    def publish(self, event: Event) -> None:
        """Pass the event to every subscriber of its class."""


class PreferenceStore(ABC):
    """On or off per player and category (R29)."""

    @abstractmethod
    def is_enabled(self, user_id: int, category: Category) -> bool:
        """True unless the player has switched the category off (A18)."""

    @abstractmethod
    def set_enabled(self, user_id: int, category: Category, enabled: bool) -> None:
        """Switch one category on or off for one player."""


class ItemCatalog(ABC):
    """The game's items, looked up by id (A11)."""

    @abstractmethod
    def get(self, item_id: str) -> Optional[Item]:
        """The item, or None if the id is unknown."""


class PlayerDirectory(ABC):
    """The platform's players, looked up by id (A12)."""

    @abstractmethod
    def display_name(self, user_id: int) -> str:
        """The player's name, or the id as text if no name is known (A25)."""


class ChallengeCatalog(ABC):
    """The game's quests and achievements, looked up by id."""

    @abstractmethod
    def get(self, challenge_id: str) -> Optional[Challenge]:
        """The challenge, or None if the id is unknown."""


class NotificationChannel(ABC):
    """A way to reach a player (R41, AD7)."""

    @abstractmethod
    def send(self, notification: Notification) -> None:
        """Hand the notification over for delivery."""
