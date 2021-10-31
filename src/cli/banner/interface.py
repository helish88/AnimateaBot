from __future__ import annotations

import abc
import typing

from src.classes import marks

if typing.TYPE_CHECKING:
    from .impl import Banner
    from .customization import DecorationContainer


__all__: tuple[str, ...] = ("BannerInterface",)


class BannerInterface(metaclass=abc.ABCMeta):
    @marks.classvar
    @abc.abstractmethod
    def decorations(_) -> DecorationContainer:
        ...

    @marks.classvar
    @abc.abstractmethod
    def raw(_) -> str:
        ...

    @classmethod
    @abc.abstractmethod
    def source(cls: typing.Type[BannerInterface]) -> Banner:
        ...
