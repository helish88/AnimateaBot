from src import enum


__all__: tuple[str, ...] = ("color", "effect", "background",)


def to_ansi(code: int) -> str:
    return AnsiEnumBase.CSI + str(code) + "m"


class AnsiEnumBase(enum.Enum):
    CSI = "\033["

    def __getitem__(self, item: str) -> str:
        return to_ansi(self.__members__[item])


@enum.only(int)
class ColorEnum(AnsiEnumBase):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37

    # Not part of the standard.
    LIGHT_BLACK = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    LIGHT_WHITE = 97


@enum.only(int)
class BackgroundEnum(AnsiEnumBase):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47

    # Not part of the standard.
    LIGHT_BLACK = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN = 106
    LIGHT_WHITE = 107


@enum.only(int)
class EffectEnum(AnsiEnumBase):
    RESET = 0
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    REVERSE = 7


color = ColorEnum()
background = BackgroundEnum()
effect = EffectEnum()
