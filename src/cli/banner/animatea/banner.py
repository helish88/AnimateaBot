from __future__ import annotations

import typing

from src.enums import color, effect
from src.classes import classes, marks
from src.cli.banner import BannerInterface, Banner, DecorationContainer


__all__: tuple[str, ...] = ("AnimateaBanner",)


@classes
class AnimateaBanner(BannerInterface):
    @marks.classvar
    def decorations(_) -> DecorationContainer:
        return DecorationContainer(
            RESET=effect["RESET"],
            CYAN=color["CYAN"],
            BLUE=color["BLUE"],
            PURPLE=color["PURPLE"],
        )

    @marks.classvar
    def raw(_) -> str:
        with open("animatea_ascii_banner.txt", "r", encoding="utf-8") as file:
            return file.read()

    @classmethod
    def source(cls: typing.Type[AnimateaBanner]) -> Banner:
        return Banner(raw_banner=cls.raw, decorations=cls.decorations)
