import typing


__all__: tuple[str, ...] = ("ClsDecorator",)


ClsDecorator = typing.Callable[[type], type]
