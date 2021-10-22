from __future__ import annotations

import typing

import hikari
import tanjun

from src.config import EnvConfig
from src.inspections import is_dunder
from src.protos import AnimateaBotProto
from src.bot.events import AnimateaEvents
from src.utils import recursive_find_path, trim_filetype

if typing.TYPE_CHECKING:
    from src.typehints import AnyCallableT

    _ClientT = typing.TypeVar("_ClientT", bound="TanjunClient")


__all__: tuple[str, ...] = (
    "TanjunClient",
    "AnimateaBot",
)


class TanjunClient(tanjun.Client):
    def load_modules(self: _ClientT) -> _ClientT:
        super().load_modules(*self._find_modules(predicate=lambda m: not is_dunder(m.name)))
        return self

    def _find_modules(self, *, predicate: AnyCallableT) -> typing.Generator[str, typing.Any, None]:
        return (
            f"src.modules.{trim_filetype(m.stem)}"
            for m in recursive_find_path("src", modify=lambda p: p.glob("modules/*.py"))
            if predicate(m)
        )


class AnimateaBot(hikari.GatewayBot, AnimateaBotProto):
    def __init__(self) -> None:
        self.config = EnvConfig()

        super().__init__(
            token=self.config["token"],
            intents=hikari.Intents.ALL,
        )

    def dispatch_events(self) -> None:
        events = AnimateaEvents(self).asdict()
        for event_type, event_impl in events.items():
            self.event_manager.subscribe(event_type, event_impl)

    def initialize(self) -> None:
        self.init_tanjun_client()
        self.dispatch_events()

        super().run(
            activity=hikari.Activity(
                name="/help",
                type=hikari.ActivityType.STREAMING,
            )
        )

    def init_tanjun_client(self) -> None:
        self.client: TanjunClient = TanjunClient.from_gateway_bot(
            self, set_global_commands=744099317836677161
        )
        self.client.load_modules()
