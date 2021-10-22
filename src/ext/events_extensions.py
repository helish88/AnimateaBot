from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import hikari

    EventImpl = typing.Callable[..., typing.Coroutine[typing.Any, typing.Any, None]]


__all__: tuple[str, ...] = ("mark",)


def mark(event_impl: EventImpl) -> EventImpl:
    setattr(event_impl, "__mark__", get_event_type(event_impl))
    return event_impl


def get_event_type(event_impl: EventImpl) -> hikari.Event:
    return typing.get_type_hints(event_impl)["event"]
