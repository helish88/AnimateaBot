from __future__ import annotations

import abc
import typing


__all__: tuple[str, ...] = ("ConverterInterface",)


class ConverterInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def convert(self, argument: typing.Any) -> typing.Any:
        ...

    @property
    @abc.abstractmethod
    def origin(self) -> type:
        ...
