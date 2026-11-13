import logging
import time

from bots.hello_bot import HelloBot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/hub.log"),
        logging.StreamHandler(),
    ],
)


def main():
    bots = [HelloBot("hello-1"), HelloBot("hello-2")]

    for bot in bots:
        bot.start()

    for cycle in range(3):
        for bot in bots:
            try:
                bot.run_once()
            except Exception as error:
                logging.error(bot.name + " failed: " + str(error))
        time.sleep(2)

    for bot in bots:
        bot.stop()
        print(bot.name, bot.status())


main()