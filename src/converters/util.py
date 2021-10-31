from __future__ import annotations

import typing

from .enums import ConvertersEnum

if typing.TYPE_CHECKING:
    from .interface import ConverterInterface
    from src.typehints import MaybeNone


__all__: tuple[str, ...] = ("get_converter_for",)


def get_converter_for(arg: typing.Any, *, convert_to: type) -> MaybeNone[ConverterInterface | type]:
    if isinstance(arg, convert_to):
        return convert_to

    for k, v in ConvertersEnum.findsource().items():
        if convert_to is k or convert_to in k:
            return typing.cast(MaybeNone[ConverterInterface], v)
