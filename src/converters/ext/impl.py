from __future__ import annotations

import typing
import asyncio
import functools

from src.converters.interface import ConverterInterface

if typing.TYPE_CHECKING:
    from src.typehints import AnyCallableT, CallableShouldReturnT

    T = typing.TypeVar("T")
    P = typing.ParamSpec("P")


__all__: tuple[str, ...] = ("has_converter",)


def has_converter(*, converter: ConverterInterface) -> CallableShouldReturnT[AnyCallableT]:
    def inner(func: typing.Callable[P, T], /) -> typing.Callable[P, T]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> typing.Any:
            if asyncio.iscoroutinefunction(func):
                callback = await func(*args, **kwargs)
            else:
                callback = func(*args, **kwargs)
            return converter.convert(callback)

        return wrapper

    return inner
