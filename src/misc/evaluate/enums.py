import enum


__all__: tuple[str, ...] = (
    "EvalBaseEnum",
    "EvalNameEnum",
)


class EvalNameEnum(str, enum.Enum):
    coro_name = "eval_coro"


class EvalBaseEnum(str, enum.Enum):
    coro_base = f"async def {EvalNameEnum.coro_name}():\n"
