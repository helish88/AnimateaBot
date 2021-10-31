import typing

from .enums import ConvertersEnum
from .interface import ConverterInterface

if typing.TYPE_CHECKING:
    ConvertersDict = dict[typing.Any, ConverterInterface]


__all__: tuple[str, ...] = ("DictBasedConverters",)


class DictBasedConverters:
    def __init__(self) -> None:
        self.__converters: ConvertersDict = {}
        self.__init_converters()

    def __init_converters(self) -> None:
        for converter, types in ConvertersEnum.findsource().items():
            self.__converters.update({types: converter})

    def register(self, *, types: typing.Any, converter: ConverterInterface) -> None:
        assert isinstance(converter, type), "converter must be a class"
        self.__converters.update({types: converter})

    @property
    def converters(self) -> ConvertersDict:
        return self.__converters
