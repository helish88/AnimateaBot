import os
import typing
import functools

from src import errors

import dotenv
dotenv.load_dotenv()


__all__: tuple[str, ...] = ("EnvConfig",)


class EnvConfig:
    def __getitem__(self, item: str) -> typing.Any:
        return self.get(item)

    def __getattr__(self, attr: str) -> typing.Any:
        return self.get(attr)

    @functools.cache
    def get(self, key: str) -> typing.Any:
        try:
            return os.environ[key]
        except KeyError as exc:
            raise errors.NonExistentKeyError(f"Key {key} not found.") from exc
