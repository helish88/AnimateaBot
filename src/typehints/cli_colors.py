import typing


__all__: tuple[str, ...] = ("AllowedColorType", "AllowedEffectType",)


AllowedColorType = typing.Literal[
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "PURPLE",
    "CYAN",
    "WHITE",
    # Not part of the standard.
    "LIGHT_BLACK",
    "LIGHT_RED",
    "LIGHT_GREEN",
    "LIGHT_YELLOW",
    "LIGHT_BLUE",
    "LIGHT_MAGENTA",
    "LIGHT_CYAN",
    "LIGHT_WHITE",
]
AllowedEffectType = typing.Literal["BOLD", "ITALIC", "UNDERLINE", "REVERSE"]
