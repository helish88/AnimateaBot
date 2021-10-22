import typing


__all__: tuple[str, ...] = ("MaybeNone",)


T = typing.TypeVar("T")
MaybeNone = typing.Union[T, None]
