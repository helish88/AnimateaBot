import logging

from .shedulers import AioIntervalScheduler


logging.basicConfig()
logging.getLogger("apscheduler").setLevel(logging.DEBUG)


def test_job() -> int:
    return 1


class Tasks:
    def __init__(self) -> None:
        self._sheduler = AioIntervalScheduler(interval=3, job=test_job)

    async def start(self) -> None:
        async with self._sheduler:
            ...
