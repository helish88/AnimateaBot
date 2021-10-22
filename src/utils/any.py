import os


__all__: tuple[str, ...] = ("on_windows",)


def on_windows() -> bool:
    """``utility function``
    Checking the current operating system.
    """
    return os.name == "nt"
