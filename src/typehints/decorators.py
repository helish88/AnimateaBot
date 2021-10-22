import typing


__all__: tuple[str, ...] = ("ClsDecoratorT",)


ClsDecoratorT = typing.TypeVar("ClsDecoratorT", bound=typing.Callable[[type], type])
