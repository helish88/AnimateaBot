from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from src.typehints import KwargsType


__all__: tuple[str, ...] = ("DecorationContainer",)


class DecorationContainer:
    def __init__(self, **kwargs: KwargsType) -> None:
        self.__kwargs = kwargs

    def __getitem__(self, item: typing.Any) -> typing.Any:
        return self.__kwargs[item]

    @property
    def members(self) -> KwargsType:
        return self.__kwargs
