import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logging.basicConfig(filename=path, level=logging.INFO,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True
                            )
        logger = logging.getLogger()
        return logger

