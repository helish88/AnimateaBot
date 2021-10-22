from __future__ import annotations

import typing

import hikari

from src.ext import events_extensions
from src.inspections import is_event

if typing.TYPE_CHECKING:
    from src.protos import AnimateaBotProto

    _EventImpl = typing.Coroutine[typing.Any, typing.Any, typing.Any]
    SubscriptionDict = dict[type, _EventImpl]


__all__: tuple[str, ...] = ("AnimateaEvents",)


class AnimateaEvents:
    def __init__(self, bot: AnimateaBotProto) -> None:
        self.bot = bot

    def asdict(self) -> SubscriptionDict:
        events: SubscriptionDict = {}
        for event_name in [i for i in dir(self) if is_event(i)]:
            impl = getattr(self, event_name)
            events[impl.__mark__] = impl
        return events

    @events_extensions.mark
    async def on_starting_event(self, event: hikari.StartingEvent) -> None:
        print("Im starting...")

    @events_extensions.mark
    async def on_started_event(self, event: hikari.StartedEvent) -> None:
        print("Im ready!")

    @events_extensions.mark
    async def on_stopping_event(self, event: hikari.StoppingEvent) -> None:
        print("Shutting down... bye-bye!")
