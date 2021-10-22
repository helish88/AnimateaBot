from __future__ import annotations

import typing

from src.enums import (
    color as color_enum,
    effect as effect_enum,
    background as background_enum,
)

if typing.TYPE_CHECKING:
    from src.typehints import MaybeNone, AllowedColorType, AllowedEffectType


__all__: tuple[str, ...] = ("cprint",)


def cprint(
    message: str,
    /,
    color: AllowedColorType,
    *,
    return_str: bool = False,
    effect: MaybeNone[AllowedEffectType] = None,
    background: MaybeNone[AllowedColorType] = None,
) -> MaybeNone[str]:
    to_print = effect_enum["RESET"] + color_enum[color]
    if background is not None:
        to_print += background_enum[background]

    if effect is not None:
        to_print += effect_enum[effect]

    final = to_print + message + effect_enum["RESET"]
    if return_str:
        return final

    print(final)
