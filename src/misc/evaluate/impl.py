from __future__ import annotations

import io
import typing
import textwrap
import traceback
import contextlib

from .enums import EvalBaseEnum, EvalNameEnum

if typing.TYPE_CHECKING:
    from src.typehints import AnyCoro


__all__: tuple[str, ...] = ("Eval",)


class Eval:
    def __init__(self, code: str, /) -> None:
        self._stdout = io.StringIO()
        self._code = textwrap.indent(self._prepare_code(code), self.tab)

    async def execute(self) -> str:
        try:
            with contextlib.redirect_stdout(self._stdout):
                result = await self._fetch_result()
        except BaseException as exc:
            result = "\n".join(traceback.format_exception(exc, exc, exc.__traceback__))  # type: ignore[arg-type]
            # Clarification: Due to the fact that in one of the functions,
            # which is implemented in the format_exception function of the
            # traceback module, there is a comparison with None, mypy thinks
            # that I somehow have to specify in the `except` that BaseException
            # is Optional[Type[BaseException]], while that the error can no
            # longer be None, and therefore Optional (because it is caught in the except).
        return result

    async def _fetch_result(self) -> str:
        return f"{self._stdout.getvalue()}\n-- {await self._get_coro()}\n"

    def _get_coro(self) -> AnyCoro:
        exec(
            EvalBaseEnum.coro_base + self._code,
            globals(),
            locals(),
        )
        return typing.cast(AnyCoro, locals()[EvalNameEnum.coro_name]())

    def _prepare_code(self, code: str, /) -> str:
        if code.startswith("```") and code.endswith("```"):
            return "\n".join(code.split("\n")[1:][:-1])
        return code

    @property
    def tab(self) -> str:
        return " " * 4
