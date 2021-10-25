from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interface to be implemented by all Observers
    """

    @abstractmethod
    def update(self, eventType, data, subject):
        pass
