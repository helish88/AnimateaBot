import typing

from src import errors


__all__: tuple[str, ...] = ("Immutable",)


class Immutable:
    def __setitem__(self, _: typing.Any, __: typing.Any) -> typing.NoReturn:
        raise errors.ObjectIsImmutableError("Enums are immutable.")

    def __setattr__(self, _: typing.Any, __: typing.Any) -> typing.NoReturn:
        raise errors.ObjectIsImmutableError("Enums are immutable.")

    def __delattr__(self, _: typing.Any) -> typing.NoReturn:
        raise errors.ObjectIsImmutableError("Enums are immutable.")

    def __delitem__(self, _: typing.Any) -> typing.NoReturn:
        raise errors.ObjectIsImmutableError("Enums are immutable.")
