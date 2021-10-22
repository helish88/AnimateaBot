import re


__all__: tuple[str, ...] = ("ANSI_ESCAPE",)


ANSI_ESCAPE: re.Pattern[str] = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
