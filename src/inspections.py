__all__: tuple[str, ...] = ("is_dunder", "is_event",)


def is_dunder(name: str) -> bool:
    return name.startswith("__")


def is_event(name: str) -> bool:
    return name.endswith("_event")
