"""The built event bus: synchronous and in one process (AD2)."""

from __future__ import annotations

import logging

from .events import Event
from .ports import EventBus, Subscriber

logger = logging.getLogger(__name__)


class InProcessEventBus(EventBus):
    """Calls each subscriber before publish() returns.

    That is what makes delivery real-time here (A21): there is no queue, no
    batch and no polling. A queue would be another EventBus implementation.
    """

    def __init__(self) -> None:
        self._subscribers: dict[type[Event], list[Subscriber]] = {}

    def subscribe(self, event_type: type[Event], subscriber: Subscriber) -> None:
        self._subscribers.setdefault(event_type, []).append(subscriber)

    def publish(self, event: Event) -> None:
        for subscriber in list(self._subscribers.get(type(event), ())):
            try:
                subscriber(event)
            except Exception:
                # AD10: a failing subscriber must never break the game or
                # social system that emitted the event.
                logger.exception("Subscriber failed for %s", type(event).__name__)
