import logging


class BaseBot:
    def __init__(self, name):
        self.name = name
        self.running = False
        self.logger = logging.getLogger(name)

    def start(self):
        self.running = True
        self.logger.info("Bot started")

    def stop(self):
        self.running = False
        self.logger.info("Bot stopped")

    def run_once(self):
        # Each bot overrides this with its own job
        raise NotImplementedError

    def status(self):
        if self.running:
            return "running"
        return "stopped"