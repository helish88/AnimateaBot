import typing


__all__: tuple[str, ...] = ("AnyCoro",)


AnyCoro = typing.Coroutine[typing.Any, typing.Any, typing.Any]
