## Design Patterns

- general repeatable solution to common scenarios in software design
- template for how to solve problem in different situations


- 3 categories
    1. Creational patterns
        - All about class instantiation
        - Can be further divided into,

            - class-creation patterns: 
                - Uses inheritance in instantiation process

            - object-creational patterns: 
                - Uses delegation to get job done

        - Types:
            - Abstract factory
                - Creates an instance of several families of classes

            - Builder
                - Separates object construction from its representation

            - Factory method
                - Creates an instance of several derived classes

            - Object pool
                - Avoid expensive acquisition and release of resources by recycling object that are no longer in use

            - Prototype
                - A fully initialized instance to be copied or cloned

            - Singleton
                - A class of which only a single instance can exist

    2. Structural patterns
        - Class and object composition
        - Use of inheritance to compose interfaces

        - Types:
            - Adapter
                - Match interfaces of different classes

            - Bridge
                - Separates an object's interface from its implementation
            
            - Composite
                - A tree structure of simple and composite objects
            
            - Decorator
                - Add responsibilities to objects dynamically
            
            - Facade
                - A signle class that represents an entire subsystem
            
            - Flyweight
                - A fine-grained instance used for efficient sharing
            
            - Private Class Data
                - Restricts accessor/mutator access
            
            - Proxy
                - An object representing another object

    3. Behavioural patterns
        - Chain of responsibility
            Request moved through serious of classes
        - Command
            Request encapsulated in command object
        - Interpreter
            Encapsulates language
        - Iterator
            Sequentially access the elements of collection
        - Mediator
            Simplifies communication among classes
        - Memento
            Capture and restore an object's internal state
        - Null object
            Represent default state for object
        - Observer
            Notify dependent class on state change
        - State
            Change behaviour on state change
        - Strategy
            Strategy encapsulates algorithm
        - Template method
            Defer the exact steps of an algorithm to a subclass
        - Visitor
            Defines a new operation to a class without change


- repository
- mvc
- mvvm


- References:
    - https://sourcemaking.com/design_patterns
    - https://refactoring.guru/design-patterns/strategy/python/example
