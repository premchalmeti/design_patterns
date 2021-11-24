from collections import defaultdict


class Subject:
    """
    This is the base class which implements,
        1. subscribers[]: array of observers whom to notify about the state changes
        2. subscribe(): to register an observer
        3. unsubscribe(): to unregister an observer
        4. notify(): called to notify subscribers
    
    The observers subscribe to the the subject to get notified of the events
    """
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event, listener):
        self.subscribers[event].append(listener)

    def unsubscribe(self, event, listener):
        self.subscribers[event].remove(listener)

    def notify(self, event, data):
        list(map(lambda s: s.update(event, data, self), self.subscribers[event]))
