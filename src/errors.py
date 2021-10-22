import hikari

from src.ext import overload_error_message


__all__: tuple[str, ...] = (
    # Bot exceptions.
    "AnimateaError",
    # Global exceptions.
    "ObjectIsNotCallableError",
    "ObjectIsImmutableError",
    "NonExistentKeyError",
    # Enums exceptions.
    "EnumError",
    "InappropriateTypeSpecifiedError",
)


@overload_error_message()
class AnimateaError(hikari.HikariError):
    """Base exception."""


# global errors
class ObjectIsNotCallableError(AnimateaError):
    """Raised when trying to invoke a non-callable object."""


class ObjectIsImmutableError(AnimateaError):
    """Raised when trying to modify an immutable object."""


class NonExistentKeyError(AnimateaError):
    """ """


# enums errors
class EnumError(AnimateaError):
    """Base exception class for enumerations."""


class InappropriateTypeSpecifiedError(EnumError):
    """Raised when the enumeration type does not match @only(type)."""
