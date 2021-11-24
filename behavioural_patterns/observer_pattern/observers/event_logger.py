import logging
import sys

from observer_pattern.observers.base_observer import Observer


class LoggingListener(Observer):
    """
    This class listens to Editor events and log it onto console
    """

    def __init__(self):
        self.logger = logging.getLogger(__file__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

    def update(self, eventType, data, subject):
        fileName = data.get('file')
        self.logger.info(f'{eventType} action is performed on {fileName}')
