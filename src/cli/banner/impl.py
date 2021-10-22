from __future__ import annotations

import typing
import dataclasses

if typing.TYPE_CHECKING:
    from .customization import DecorationContainer


__all__: tuple[str, ...] = ("Banner",)


@dataclasses.dataclass()
class Banner:
    raw_banner: str
    decorations: DecorationContainer

    def __replace_color_codes(self) -> None:
        for member, ansi in self.decorations.members.items():
            self.raw_banner = self.raw_banner.replace(f"${member}$", ansi)

    def show(self) -> None:
        self.__replace_color_codes()
        print(self.raw_banner)
