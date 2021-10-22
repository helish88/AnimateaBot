import typing

import hikari


__all__: tuple[str, ...] = ("AnimateaBotProto",)


class AnimateaBotProto(hikari.GatewayBotAware, typing.Protocol):
    def dispatch_events(self) -> None:
        raise NotImplementedError

    def initialize(self) -> None:
        raise NotImplementedError

    def init_tanjun_client(self) -> None:
        raise NotImplementedError
