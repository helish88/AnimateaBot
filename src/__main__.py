
<<<<<<< HEAD

parser = argparse.ArgumentParser()
parser.add_argument(
    "--mypy",
    action="store_true",
)
namespace = parser.parse_args()
if namespace.mypy:
    os.system("mypy --no-site-packages --config-file=pyproject.toml src")
=======
>>>>>>> 00058ea7ee9f632ba1778e5acc51aff053c0cc4b
