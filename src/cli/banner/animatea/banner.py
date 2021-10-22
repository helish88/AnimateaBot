from src.enums import color, effect
from src.cli.banner import AbstractBanner, Banner, DecorationContainer


__all__: tuple[str, ...] = ("AnimateaBanner",)


class AnimateaBanner(AbstractBanner):
    @property
    def decorations(self) -> DecorationContainer:
        return DecorationContainer(
            RESET=effect["RESET"],
            CYAN=color["CYAN"],
            BLUE=color["BLUE"],
            PURPLE=color["PURPLE"],
        )

    @property
    def raw(self) -> str:
        with open("animatea_ascii_banner.txt", "r", encoding="utf-8") as file:
            return file.read()

    @property
    def source(self) -> Banner:
        return Banner(raw_banner=self.raw, decorations=self.decorations)
