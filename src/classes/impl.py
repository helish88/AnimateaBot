from __future__ import annotations

import typing

from .inspections import is_classvar

if typing.TYPE_CHECKING:
    ClassT = typing.TypeVar("ClassT", bound=type)


__all__: tuple[str, ...] = ("classes",)


def classes(cls: ClassT) -> ClassT:
    for method in dir(cls):
        if is_classvar(classvar := getattr(cls, method)):
            setattr(cls, method, classvar(...))
    return cls
