from core.base_bot import BaseBot


class HelloBot(BaseBot):
    def run_once(self):
        self.logger.info("Hello from " + self.name)