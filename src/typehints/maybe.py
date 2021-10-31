import typing


__all__: tuple[str, ...] = (
    "MaybeNone",
    "MaybeNoReturn",
)


T = typing.TypeVar("T")
MaybeNone = typing.Union[T, None]
MaybeNoReturn = typing.Union[T, typing.NoReturn]
