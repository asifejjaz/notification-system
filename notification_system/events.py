"""Events the platform emits. This module imports nothing from the project.

Each event is an immutable fact. In every event with two players, the player
who acted comes first, as in the brief's friendRequestSent(3, 1).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    """Base class for everything published on the event bus."""


# Game events (R15)


@dataclass(frozen=True)
class PlayerLeveledUp(Event):
    user_id: int
    level: int


@dataclass(frozen=True)
class ItemAcquired(Event):
    user_id: int
    item_id: str


@dataclass(frozen=True)
class ChallengeCompleted(Event):
    user_id: int
    challenge_id: str


# Social events (R20)


@dataclass(frozen=True)
class FriendRequestSent(Event):
    sender_id: int
    recipient_id: int


@dataclass(frozen=True)
class FriendRequestAccepted(Event):
    accepter_id: int
    requester_id: int


@dataclass(frozen=True)
class FollowerAdded(Event):
    follower_id: int
    followed_id: int
