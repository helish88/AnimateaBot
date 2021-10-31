import typing

from .interface import ConverterInterface


__all__: tuple[str, ...] = ("SimpleConverter",)


class SimpleConverter(ConverterInterface):
    def __init__(self, *, type: type) -> None:
        self.__type = type

    def convert(self, argument: typing.Any) -> typing.Any:
        return self.__type(argument)

    @property
    def origin(self) -> type:
        return self.__type
