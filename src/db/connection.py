from __future__ import annotations

import typing

import asyncpg

from src.utils import Yaml

if typing.TYPE_CHECKING:
    from asyncio import AbstractEventLoop


from_yaml = Yaml.load("config").filter("db")


async def create_pool(loop: AbstractEventLoop) -> asyncpg.Pool:
    async with asyncpg.create_pool(loop=loop, **from_yaml) as pool:
        return pool
