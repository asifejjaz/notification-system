"""In-memory stores (AD6, A23). Nothing here survives a restart.

Each one maps to a table in docs/architecture.md, section 6.
"""

from __future__ import annotations

from typing import Iterable, Mapping, Optional

from .domain import Category, Challenge, Item
from .ports import ChallengeCatalog, ItemCatalog, PlayerDirectory, PreferenceStore


class InMemoryPreferenceStore(PreferenceStore):
    """Preferences in a dictionary, which the brief allows (R30)."""

    def __init__(self) -> None:
        self._enabled: dict[int, dict[Category, bool]] = {}

    def is_enabled(self, user_id: int, category: Category) -> bool:
        # A18: enabled unless the player has switched the category off.
        return self._enabled.get(user_id, {}).get(category, True)

    def set_enabled(self, user_id: int, category: Category, enabled: bool) -> None:
        self._enabled.setdefault(user_id, {})[category] = enabled


class InMemoryPlayerDirectory(PlayerDirectory):
    """Stand-in for the platform's player data (A12)."""

    def __init__(self, names: Optional[Mapping[int, str]] = None) -> None:
        self._names = dict(names or {})

    def display_name(self, user_id: int) -> str:
        # A25: a player with no known name is shown by id.
        return self._names.get(user_id, str(user_id))


class InMemoryItemCatalog(ItemCatalog):
    """Stand-in for the game's item data (A11)."""

    def __init__(self, items: Iterable[Item] = ()) -> None:
        self._items = {item.id: item for item in items}

    def get(self, item_id: str) -> Optional[Item]:
        return self._items.get(item_id)


class InMemoryChallengeCatalog(ChallengeCatalog):
    """Stand-in for the game's quest and achievement data."""

    def __init__(self, challenges: Iterable[Challenge] = ()) -> None:
        self._challenges = {challenge.id: challenge for challenge in challenges}

    def get(self, challenge_id: str) -> Optional[Challenge]:
        return self._challenges.get(challenge_id)
