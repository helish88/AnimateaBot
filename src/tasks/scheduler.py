from __future__ import annotations

import pytz
import typing

from apscheduler.schedulers.asyncio import AsyncIOScheduler

if typing.TYPE_CHECKING:
    import types

    from src.typehints import MaybeNone, AnyCallableT


__all__: tuple[str, ...] = ("AioIntervalScheduler",)


class AioIntervalScheduler:
    def __init__(self, *, job: AnyCallableT, interval: int, paused: bool = False) -> None:
        self._job = job
        self._paused = paused
        self._interval = interval

    async def __aenter__(self) -> None:
        self._init_scheduler()
        self.scheduler.start(paused=self._paused)

    @typing.overload
    async def __aexit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        ...

    @typing.overload
    async def __aexit__(
        self,
        exc_type: typing.Type[BaseException],
        exc_val: BaseException,
        exc_tb: types.TracebackType,
    ) -> None:
        ...

    async def __aexit__(
        self,
        exc_type: MaybeNone[typing.Type[BaseException]],
        exc_val: MaybeNone[BaseException],
        exc_tb: MaybeNone[types.TracebackType],
    ) -> None:
        self.scheduler.remove_all_jobs()
        self.scheduler.shutdown()

    def _init_scheduler(self) -> None:
        self.scheduler = AsyncIOScheduler(timezone=pytz.utc)
        self.scheduler.add_job(self._job, "interval", seconds=self._interval)
