from __future__ import annotations

import enum
import typing

from .impl import SimpleConverter

if typing.TYPE_CHECKING:
    from src.typehints import AnyDict


__all__: tuple[str, ...] = ("ConvertersEnum",)


class ConvertersEnum(tuple[typing.Any], enum.Enum):
    base = (str, int, bool, list, dict), SimpleConverter

    @classmethod
    def findsource(cls: typing.Type[ConvertersEnum]) -> AnyDict:
        return dict(cls.__members__.values())  # type: ignore[arg-type]
        # Clarification: mypy for some reason does not see ValuesView as an iterable object.
