"""The dispatcher: the same steps for every event (R38 to R41)."""

from __future__ import annotations

import logging
from typing import Iterable

from .events import Event
from .ports import NotificationChannel, PreferenceStore
from .rules import NotificationRule

logger = logging.getLogger(__name__)


class NotificationService:
    """Turns events into notifications and sends them.

    It knows no event type by name. Everything specific to an event type is in
    its rule, so this class does not change when an event type is added (R34).
    """

    def __init__(
        self,
        rules: Iterable[NotificationRule],
        preferences: PreferenceStore,
        channels: Iterable[NotificationChannel],
    ) -> None:
        # AD9: a list of rules per event class, so one event can notify twice.
        self._rules: dict[type[Event], list[NotificationRule]] = {}
        for rule in rules:
            self._rules.setdefault(rule.event_type, []).append(rule)
        self._preferences = preferences
        self._channels = list(channels)  # AD7: one entry today, the in-app channel

    @property
    def event_types(self) -> tuple[type[Event], ...]:
        """The event classes that have at least one rule."""
        return tuple(self._rules)

    def handle(self, event: Event) -> None:
        """Process one event. This is what the bus calls (R35)."""
        rules = self._rules.get(type(event), [])
        if not rules:
            logger.debug("IGNORED %s: no rule", type(event).__name__)
        for rule in rules:
            self._dispatch(rule, event)

    def _dispatch(self, rule: NotificationRule, event: Event) -> None:
        # R38: the rule fixes the type, and the type fixes the category.
        notification_type = rule.notification_type
        recipient_id = rule.recipient_id(event)

        # R40, before R39 (AD3). The check needs only the recipient and the
        # category, so a blocked notification costs no lookup and no object.
        # To follow the order of the brief's sentence, move this block below
        # rule.create().
        category = notification_type.category
        if not self._preferences.is_enabled(recipient_id, category):
            # A20: dropped. Not stored, not sent later.
            logger.info(
                "SKIPPED %s for user %s: '%s' is disabled",
                notification_type.name, recipient_id, category.label,
            )
            return

        # R39: the rule creates the Notification, or nothing if the event
        # does not qualify (for example an item below rare, A10).
        notification = rule.create(event)
        if notification is None:
            logger.info(
                "SKIPPED %s for user %s: the event does not qualify",
                notification_type.name, recipient_id,
            )
            return

        # R41: send on every channel.
        for channel in self._channels:
            try:
                channel.send(notification)
            except Exception:
                # AD10: one failing channel must not block the next one.
                logger.exception(
                    "FAILED %s for user %s on %s",
                    notification_type.name, recipient_id, type(channel).__name__,
                )
            else:
                logger.debug(
                    "SENT %s to user %s on %s",
                    notification_type.name, recipient_id, type(channel).__name__,
                )
