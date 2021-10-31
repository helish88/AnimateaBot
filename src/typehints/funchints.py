import types
import typing


__all__: tuple[str, ...] = ("FunctionOrCoroutine",)


FunctionOrCoroutine = typing.Union[types.FunctionType, types.CoroutineType]
