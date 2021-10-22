from __future__ import annotations

import typing
import pathlib
import dataclasses
import collections.abc

import yaml

if typing.TYPE_CHECKING:
    from src.typehints import AnyCallableT

    T = typing.TypeVar("T")
    _DictKeyOr = typing.Union[typing.Hashable, T]


__all__: tuple[str, ...] = ("Yaml",)


@dataclasses.dataclass()
class Yaml:
    data: typing.Any

    def filter(self, predicate: _DictKeyOr[AnyCallableT] = None, /) -> typing.Any:
        if isinstance(predicate, collections.abc.Hashable):
            return self.data[predicate]
        elif isinstance(predicate, collections.abc.Callable):
            return predicate(self.data)
        else:
            return self.data

    @staticmethod
    def cwd() -> str:
        return str(pathlib.Path(__file__).parents[1]) + "\\"

    @classmethod
    def load(cls, filename: str, /) -> typing.Any:
        with open(cls.cwd() + (filename + ".yaml"), "r", encoding="utf-8") as file:
            return cls(yaml.safe_load(file))
