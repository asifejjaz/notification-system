"""Each event type sends the right text to the right player.

The tests fire the same triggers the brief gives (R44) through the wired
system, and read what the simulated in-app channel recorded.
"""

import io
import unittest

from notification_system.bootstrap import build_app
from notification_system.domain import Category, Notification, NotificationType


class EventTypeTests(unittest.TestCase):
    def setUp(self) -> None:
        # The channel prints what it sends. A buffer keeps the test output quiet.
        self.app = build_app(stream=io.StringIO())
        self.game_engine = self.app.game_engine
        self.social_system = self.app.social_system

    def only_notification(self) -> Notification:
        self.assertEqual(len(self.app.in_app.delivered), 1)
        return self.app.in_app.delivered[0]

    def assert_nothing_sent(self) -> None:
        self.assertEqual(self.app.in_app.delivered, [])

    # --- the six event types: right player, right type ---

    def test_R16_level_up_notifies_the_player_who_levelled_up(self) -> None:
        self.game_engine.playerLeveledUp(1, 15)
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 1)
        self.assertIs(notification.type, NotificationType.LEVEL_UP)
        self.assertIs(notification.category, Category.GAME_EVENTS)

    def test_R17_rare_item_notifies_the_player_who_got_it(self) -> None:
        self.game_engine.itemAcquired(2, "SwordOfAzeroth")
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 2)
        self.assertIs(notification.type, NotificationType.ITEM_ACQUIRED)
        self.assertIs(notification.category, Category.GAME_EVENTS)

    def test_R18_challenge_completed_notifies_the_player_who_completed_it(self) -> None:
        self.game_engine.challengeCompleted(1, "DragonSlayer")
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 1)
        self.assertIs(notification.type, NotificationType.CHALLENGE_COMPLETED)
        self.assertEqual(notification.message, "You've completed the challenge 'Dragon Slayer'!")

    def test_R21_friend_request_notifies_the_player_it_was_sent_to(self) -> None:
        self.social_system.friendRequestSent(3, 1)
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 1)
        self.assertIs(notification.type, NotificationType.FRIEND_REQUEST)
        self.assertIs(notification.category, Category.SOCIAL_EVENTS)

    def test_R22_A14_friend_accepted_notifies_the_requester_not_the_accepter(self) -> None:
        # User 1 accepted the request from user 3, so user 3 is told.
        self.social_system.friendRequestAccepted(1, 3)
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 3)
        self.assertIs(notification.type, NotificationType.FRIEND_ACCEPTED)
        self.assertEqual(notification.message, "Player 'Aria' has accepted your friend request.")

    def test_R23_new_follower_notifies_the_player_who_was_followed(self) -> None:
        self.social_system.followerAdded(2, 1)
        notification = self.only_notification()
        self.assertEqual(notification.recipient_id, 1)
        self.assertIs(notification.type, NotificationType.NEW_FOLLOWER)
        self.assertEqual(notification.message, "Player 'Borin' has started following you.")

    # --- the brief's three sample texts, word for word ---

    def test_R26_level_up_text_matches_the_brief(self) -> None:
        self.game_engine.playerLeveledUp(1, 15)
        self.assertEqual(self.only_notification().message, "Congratulations! You've reached level 15!")

    def test_R27_item_acquired_text_matches_the_brief(self) -> None:
        # The trigger carries only "SwordOfAzeroth". The word "legendary" and
        # the name "Sword of Azeroth" come from the item catalog (A11).
        self.game_engine.itemAcquired(2, "SwordOfAzeroth")
        self.assertEqual(self.only_notification().message, "You've acquired the legendary Sword of Azeroth!")

    def test_R28_friend_request_text_matches_the_brief(self) -> None:
        # The brief writes Player 'X'. X is the sender's display name (A12).
        self.social_system.friendRequestSent(3, 1)
        self.assertEqual(self.only_notification().message, "Player 'Cyra' has sent you a friend request.")

    def test_R44_the_four_triggers_from_the_brief_each_notify_one_player(self) -> None:
        self.game_engine.playerLeveledUp(1, 15)
        self.game_engine.itemAcquired(2, "SwordOfAzeroth")
        self.social_system.friendRequestSent(3, 1)
        self.social_system.friendRequestAccepted(1, 3)
        self.assertEqual([n.recipient_id for n in self.app.in_app.delivered], [1, 2, 1, 3])

    # --- events that must send nothing ---

    def test_A10_item_below_rare_sends_nothing(self) -> None:
        self.game_engine.itemAcquired(2, "WoodenShield")  # a common item
        self.assert_nothing_sent()

    def test_A25_unknown_item_sends_nothing(self) -> None:
        self.game_engine.itemAcquired(2, "NoSuchItem")
        self.assert_nothing_sent()

    def test_A25_player_with_no_known_name_is_shown_by_id(self) -> None:
        self.social_system.friendRequestSent(99, 1)
        self.assertEqual(self.only_notification().message, "Player '99' has sent you a friend request.")


if __name__ == "__main__":
    unittest.main()
