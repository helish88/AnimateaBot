from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from src.typehints import AnyCallableT


__all__: tuple[str, ...] = ("classvar",)


def classvar(impl: AnyCallableT) -> typing.Any:
    setattr(impl, "__classvar__", True)
    return impl
