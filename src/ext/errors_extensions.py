from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from src.typehints import ClsDecorator


__all__: tuple[str, ...] = ("overload_error_message",)


_DEFAULT_ERRMSG_TEMPLATE: typing.Final[
    str
] = "An error was thrown for the following reason -> "


def overload_error_message(*, template: str = _DEFAULT_ERRMSG_TEMPLATE) -> ClsDecorator:
    def inner(cls: type) -> type:
        cls.__str__ = lambda self: (  # type: ignore # mypy can't understand this.
            f"\n"
            # Skipping to new line.
            f"{template}"
            # Using template in at the beginning of the error message.
            + f"{self.args[0]}\n"
            # An error message is always expected as the first argument
            # (at the convention level, there may be exceptions).
            + (" " * len(template))
            # Multiply by the length of the template to highlight the error text.
            + ("^" * len(self.args[0]))
            # Creating arrows to highlight the error.
        )
        return cls
    return inner
