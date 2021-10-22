import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--mypy",
    action="store_true",
)
namespace = parser.parse_args()
if namespace.mypy:
    os.system("mypy --no-site-packages --config-file=../pyproject.toml ../src")