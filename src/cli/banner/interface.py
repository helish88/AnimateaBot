from __future__ import annotations

import abc
import typing

if typing.TYPE_CHECKING:
    from .impl import Banner
    from .customization import DecorationContainer


__all__: tuple[str, ...] = ("AbstractBanner",)


class AbstractBanner(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def decorations(self) -> DecorationContainer:
        ...

    @property
    @abc.abstractmethod
    def raw(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def source(self) -> Banner:
        ...
