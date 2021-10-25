from observer_pattern.observers.base_observer import Observer


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
        self.subscribers = {}

    def subscribe(self, eventType, listener):
        eventSubscribers = self.subscribers.get(eventType, [])
        eventSubscribers.append(listener)
        self.subscribers[eventType] = eventSubscribers

    def unsubscribe(self, eventType, listener):
        self.subscribers[eventType] = filter(lambda s: s != listener, self.subscribers.get(eventType, []))

    def notify(self, eventType, data):
        list(map(lambda s: s.update(eventType, data, self), self.subscribers.get(eventType, [])))
