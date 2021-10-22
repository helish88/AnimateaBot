from __future__ import annotations

import typing
import pathlib

if typing.TYPE_CHECKING:
    from src.typehints import MaybeNone, AnyCallableT


__all__: tuple[str, ...] = (
    "recursive_find_path",
    "trim_filetype",
    "get_cwd",
)


def recursive_find_path(
    to_find: str,
    /,
    *,
    modify: MaybeNone[AnyCallableT] = None,
    curdir: pathlib.Path = pathlib.Path(__file__),
) -> typing.Any:
    parent = curdir.parent
    if parent.name.endswith(to_find):
        if modify is not None:
            return modify(parent)
        return parent
    else:
        return recursive_find_path(to_find, curdir=parent, modify=modify)


def trim_filetype(name: str, /) -> str:
    if name.endswith(".py"):
        return name[:-3]
    return name


def get_cwd() -> str:
    return str(pathlib.Path(__file__).parents[1]) + "\\"
