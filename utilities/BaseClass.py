import inspect
import logging
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        logMethodName = inspect.stack()[1][3] # Prints the method name of the pytest script
        logger = logging.getLogger(logMethodName)
        # Set Log Formatter
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        # FileHnadler object
        fileHandler = logging.FileHandler('logs/logFile.log')
        # Attahing Log formatter to FileHandler
        fileHandler.setFormatter(formatter)

        # Attaching the fileHandler to logger
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger