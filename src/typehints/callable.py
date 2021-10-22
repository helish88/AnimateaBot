import typing


__all__: tuple[str, ...] = (
    "AnyCallableT",
    "CallableShouldReturnT",
)


T = typing.TypeVar("T")

AnyCallableT = typing.TypeVar("AnyCallableT", bound=typing.Callable[..., typing.Any])
CallableShouldReturnT = typing.Callable[..., T]
