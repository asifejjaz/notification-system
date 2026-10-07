"""User preferences: on or off per player and category (R29)."""

import io
import unittest

from notification_system.bootstrap import build_app
from notification_system.bus import InProcessEventBus
from notification_system.channels import InAppChannel
from notification_system.domain import Category
from notification_system.memory import InMemoryPreferenceStore
from notification_system.ports import PlayerDirectory
from notification_system.rules import FriendRequestRule
from notification_system.service import NotificationService
from notification_system.simulation import SocialSystem


class CountingPlayerDirectory(PlayerDirectory):
    """A fake that counts lookups, to prove when none is made."""

    def __init__(self) -> None:
        self.lookups = 0

    def display_name(self, user_id: int) -> str:
        self.lookups += 1
        return f"Player{user_id}"


class PreferenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = build_app(stream=io.StringIO())
        self.delivered = self.app.in_app.delivered

    def test_A18_every_category_is_enabled_by_default(self) -> None:
        for category in Category:
            self.assertTrue(self.app.preferences.is_enabled(1, category))
        # Nobody has set a preference, and both categories still send.
        self.app.game_engine.playerLeveledUp(1, 15)
        self.app.social_system.friendRequestSent(3, 1)
        self.assertEqual(len(self.delivered), 2)

    def test_R29_disabled_category_sends_nothing(self) -> None:
        self.app.preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)
        self.app.social_system.friendRequestSent(3, 1)
        self.assertEqual(self.delivered, [])

    def test_R29_preference_is_per_category(self) -> None:
        self.app.preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)
        self.app.game_engine.playerLeveledUp(1, 15)  # Game Events are still on
        self.assertEqual([n.recipient_id for n in self.delivered], [1])

    def test_R29_preference_is_per_user(self) -> None:
        self.app.preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)
        self.app.social_system.friendRequestAccepted(1, 3)  # goes to user 3
        self.assertEqual([n.recipient_id for n in self.delivered], [3])

    def test_R29_A20_enabling_again_sends_new_events_only(self) -> None:
        self.app.preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)
        self.app.social_system.friendRequestSent(2, 1)  # dropped
        self.app.preferences.set_enabled(1, Category.SOCIAL_EVENTS, True)
        self.assertEqual(self.delivered, [])  # A20: the dropped one is not sent later
        self.app.social_system.friendRequestSent(2, 1)
        self.assertEqual(len(self.delivered), 1)

    def test_AD3_disabled_category_sends_nothing_and_makes_no_lookup(self) -> None:
        # Wired by hand so the player directory can be a counting fake.
        bus = InProcessEventBus()
        preferences = InMemoryPreferenceStore()
        players = CountingPlayerDirectory()
        channel = InAppChannel(io.StringIO())
        service = NotificationService([FriendRequestRule(players)], preferences, [channel])
        for event_type in service.event_types:
            bus.subscribe(event_type, service.handle)
        social_system = SocialSystem(bus)

        preferences.set_enabled(1, Category.SOCIAL_EVENTS, False)
        social_system.friendRequestSent(3, 1)
        self.assertEqual(channel.delivered, [])
        self.assertEqual(players.lookups, 0)  # checked before create (AD3)

        preferences.set_enabled(1, Category.SOCIAL_EVENTS, True)
        social_system.friendRequestSent(3, 1)
        self.assertEqual(len(channel.delivered), 1)
        self.assertEqual(players.lookups, 1)


if __name__ == "__main__":
    unittest.main()
