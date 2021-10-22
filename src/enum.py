from __future__ import annotations

import typing

from src import errors
from src.bases import Immutable
from src.inspections import is_dunder

if typing.TYPE_CHECKING:
    from src.typehints import ClsDecorator


__all__: tuple[str, ...] = (
    "Enum",
    "only",
)


def only(type_: type, /) -> ClsDecorator:
    def inner(cls: type) -> type:
        for key, value in cls.__dict__.items():
            if not is_dunder(key) and not isinstance(value, type_):
                raise errors.InappropriateTypeSpecifiedError(
                    f"This type does not match the global enumeration type. "
                    f"(Expected {type_}, got {type(value)})"
                )
        return cls

    return inner


class EnumBase(Immutable):
    if typing.TYPE_CHECKING:
        __members__: dict[str, typing.Any]

    def __getitem__(self, item: str) -> typing.Any:
        return self.__members__[item]

    def __len__(self) -> int:
        return len(self.__members__)

    def __repr__(self) -> str:
        inner = ", ".join(f"{k}={v}" for k, v in self.__members__.items())
        return f"<Enum({inner})>"


class EnumMeta(type):
    def __new__(
        mcs: typing.Type[EnumMeta],
        name: str,
        bases: tuple[type, ...],
        attrs: dict[str, typing.Any],
    ) -> EnumMeta:
        try:
            filter_ = attrs["__filter__"]
            if not callable(filter_):
                raise errors.ObjectIsNotCallableError("Callable object expected.")
        except KeyError:
            filter_ = lambda _: True

        members = {}
        for member in [m for m in attrs if not is_dunder(m) and filter_(m)]:
            members.update({member: attrs[member]})

        if bases:
            bases += (EnumBase,)

        attrs["__members__"] = members
        return super().__new__(mcs, name, bases, attrs)


class Enum(metaclass=EnumMeta):
    if typing.TYPE_CHECKING:
        __members__: dict[str, typing.Any]
