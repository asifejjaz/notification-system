"""Delivery channels. Only in-app is built (R24, N3)."""

from __future__ import annotations

import sys
from typing import Optional, TextIO

from .domain import Notification
from .ports import NotificationChannel


class InAppChannel(NotificationChannel):
    """Stand-in for the game client's own notification mechanism (N2, R45).

    The brief says that mechanism exists and can be mocked. This one prints
    each notification and keeps it, so the demo can show it and tests can
    read it.
    """

    def __init__(self, stream: Optional[TextIO] = None) -> None:
        self._stream = stream
        self.delivered: list[Notification] = []

    def send(self, notification: Notification) -> None:
        self.delivered.append(notification)
        print(
            f"SENT    in-app to user {notification.recipient_id}: {notification.message}",
            file=self._stream if self._stream is not None else sys.stdout,
        )
