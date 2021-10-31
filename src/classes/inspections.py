from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from src.typehints import AnyCallableT


__all__: tuple[str, ...] = ("is_classvar",)


def is_classvar(fn: AnyCallableT) -> bool:
    return hasattr(fn, "__classvar__")
