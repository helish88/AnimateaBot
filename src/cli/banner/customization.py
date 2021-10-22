from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from src.typehints import AnyValueDict


__all__: tuple[str, ...] = ("DecorationContainer",)


class DecorationContainer:
    def __init__(self, **kwargs: AnyValueDict) -> None:
        self.__kwargs = kwargs

    def __getitem__(self, item: typing.Any) -> typing.Any:
        return self.__kwargs[item]

    @property
    def members(self) -> AnyValueDict:
        return self.__kwargs
