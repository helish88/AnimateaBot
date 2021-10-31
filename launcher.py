from src.cli.banner.animatea import AnimateaBanner
from src.bot.main import AnimateaBot


if __name__ == "__main__":
    AnimateaBanner.source().show()

    bot = AnimateaBot()
    bot.initialize()
