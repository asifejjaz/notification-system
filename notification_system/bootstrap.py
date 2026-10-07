"""The composition root: the only place that wires things together (AD5).

To use a database, a queue or another channel, change what is built here.
Nothing else needs to know.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TextIO

from .bus import InProcessEventBus
from .channels import InAppChannel
from .domain import Challenge, Item, Rarity
from .memory import (
    InMemoryChallengeCatalog,
    InMemoryItemCatalog,
    InMemoryPlayerDirectory,
    InMemoryPreferenceStore,
)
from .ports import EventBus, PreferenceStore
from .rules import default_rules
from .service import NotificationService
from .simulation import GameEngine, SocialSystem

# Sample data for the simulated platform. The brief's triggers use players
# 1, 2 and 3 and the item "SwordOfAzeroth".
SAMPLE_PLAYERS = {1: "Aria", 2: "Borin", 3: "Cyra"}
SAMPLE_ITEMS = (
    Item("SwordOfAzeroth", "Sword of Azeroth", "A blade from the first age.", Rarity.LEGENDARY),
    Item("WoodenShield", "Wooden Shield", "A plain training shield.", Rarity.COMMON),
)
SAMPLE_CHALLENGES = (Challenge("DragonSlayer", "Dragon Slayer"),)


@dataclass(frozen=True)
class App:
    """The wired system, as the demo and the tests use it."""

    game_engine: GameEngine
    social_system: SocialSystem
    preferences: PreferenceStore
    in_app: InAppChannel
    bus: EventBus
    service: NotificationService


def build_app(stream: Optional[TextIO] = None) -> App:
    """Build the whole system. The in-app channel prints to stream, or to stdout."""
    bus = InProcessEventBus()
    preferences = InMemoryPreferenceStore()
    players = InMemoryPlayerDirectory(SAMPLE_PLAYERS)
    items = InMemoryItemCatalog(SAMPLE_ITEMS)
    challenges = InMemoryChallengeCatalog(SAMPLE_CHALLENGES)
    in_app = InAppChannel(stream)

    # R24: in-app is the only channel.
    service = NotificationService(default_rules(players, items, challenges), preferences, [in_app])

    # R36: the service receives every event class that has a rule.
    for event_type in service.event_types:
        bus.subscribe(event_type, service.handle)

    return App(GameEngine(bus), SocialSystem(bus), preferences, in_app, bus, service)
