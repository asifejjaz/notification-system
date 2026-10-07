"""The bus and the dispatcher: unknown events, failures, several rules."""

import io
import unittest
from dataclasses import dataclass
from typing import Optional

from notification_system.bootstrap import build_app
from notification_system.bus import InProcessEventBus
from notification_system.channels import InAppChannel
from notification_system.domain import Notification, NotificationType
from notification_system.events import Event, FriendRequestAccepted, PlayerLeveledUp
from notification_system.memory import InMemoryPlayerDirectory, InMemoryPreferenceStore
from notification_system.ports import NotificationChannel
from notification_system.rules import FriendAcceptedRule, LevelUpRule, NotificationRule
from notification_system.service import NotificationService
from notification_system.simulation import GameEngine


@dataclass(frozen=True)
class ServerRestarted(Event):
    """An event class that no rule is registered for."""


class FailingChannel(NotificationChannel):
    def send(self, notification: Notification) -> None:
        raise RuntimeError("the channel is down")


class AccepterConfirmationRule(NotificationRule):
    """A second rule for an event class that already has one. Test only."""

    event_type = FriendRequestAccepted
    notification_type = NotificationType.FRIEND_ACCEPTED

    def recipient_id(self, event: FriendRequestAccepted) -> int:
        return event.accepter_id

    def create(self, event: FriendRequestAccepted) -> Optional[Notification]:
        return self._notification(event, "You are now friends.")


class DispatchTests(unittest.TestCase):
    def test_R35_event_with_no_rule_is_ignored(self) -> None:
        app = build_app(stream=io.StringIO())
        app.bus.publish(ServerRestarted())  # nobody is subscribed
        app.service.handle(ServerRestarted())  # and the service has no rule
        self.assertEqual(app.in_app.delivered, [])

    def test_AD10_failing_subscriber_does_not_break_the_emitter(self) -> None:
        bus = InProcessEventBus()
        received: list[Event] = []

        def failing_subscriber(event: Event) -> None:
            raise RuntimeError("the subscriber is broken")

        bus.subscribe(PlayerLeveledUp, failing_subscriber)
        bus.subscribe(PlayerLeveledUp, received.append)

        with self.assertLogs("notification_system.bus", level="ERROR") as logs:
            GameEngine(bus).playerLeveledUp(1, 15)  # must not raise

        self.assertEqual(received, [PlayerLeveledUp(1, 15)])  # the next subscriber still ran
        self.assertIn("Subscriber failed for PlayerLeveledUp", logs.output[0])

    def test_AD10_failing_channel_does_not_block_the_next_one(self) -> None:
        working = InAppChannel(io.StringIO())
        service = NotificationService([LevelUpRule()], InMemoryPreferenceStore(), [FailingChannel(), working])

        with self.assertLogs("notification_system.service", level="ERROR") as logs:
            service.handle(PlayerLeveledUp(1, 15))  # must not raise

        self.assertEqual(len(working.delivered), 1)
        self.assertIn("FAILED LEVEL_UP for user 1 on FailingChannel", logs.output[0])

    def test_AD9_two_rules_on_one_event_class_both_run(self) -> None:
        players = InMemoryPlayerDirectory({1: "Aria", 3: "Cyra"})
        channel = InAppChannel(io.StringIO())
        service = NotificationService(
            [FriendAcceptedRule(players), AccepterConfirmationRule()],
            InMemoryPreferenceStore(),
            [channel],
        )

        service.handle(FriendRequestAccepted(1, 3))

        self.assertEqual([n.recipient_id for n in channel.delivered], [3, 1])
        self.assertEqual(
            [n.message for n in channel.delivered],
            ["Player 'Aria' has accepted your friend request.", "You are now friends."],
        )


if __name__ == "__main__":
    unittest.main()
