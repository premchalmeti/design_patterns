# Observer pattern:
    1. Subject:
        - Often called as publisher implements a subscription mechanism
        - Implementation contains,
            1. subscribers[]: array of observers whom to notify about the state changes
            2. subscribe(): to register an observer
            3. unsubscribe(): to unregister an observer
            4. notify(): called to notify subscribers

    2. Observer:
        - Subscribe to a Subject to listen to all events
        - All the observers implement some common interface and override `update()` method
        - The subscriber calls `update()` method to notify observers
