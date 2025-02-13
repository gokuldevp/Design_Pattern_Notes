"""
The Singleton Pattern is grounded in the principle of ensuring a class has only one instance, and provides a global point of access to that instance

Concept Explanation:
1. Unique Instance: The fundamental idea is to guarantee that a class has a single, unique instance. This is useful when exactly one object is needed to coordinate actions across the system (like managing a connection pool or a shared resource).
2. Controlled Access Point: The Singleton provides a controlled access point, meaning it allows the system to have a centralized point from where the single instance can be accessed. This is managed through a static method that returns the instance.
3. Lazy Initialization: The Singleton instance is created only when it is needed (also known as lazy initialization). This helps in optimizing resource usage because the instance is created only when it's actually required.

Components of Singleton Pattern:
1. Private Constructor: Prevents the instantiation of the class from outside.
2. Static Variable: Holds the single instance of the class.
3. Static Method: Returns the single instance, creating it if it doesn't exist.

Examples:
1. Think of it as having a single controller in a game console. No matter how many times you need a controller, you'll always use that single controller.
2. consider a configuration manager in an application – you’d want a single configuration manager that manages all configurations, ensuring consistency and ease of access.
3. Caching: The Singleton or Borg Pattern can be used to maintain a cache of information that needs to be accessed by various parts of a system without repeatedly fetching it from the original source.

Note: The Borg pattern (also known as the Monostate pattern) is an alternative to the Singleton Pattern that achieves a similar goal but in a different way.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True


# The Borg pattern
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton1(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

# Usage
singleton1 = Singleton1(a=1, b=2)
singleton2 = Singleton1(c=3)

print(singleton1)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(singleton2)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(singleton1 is singleton2)  # Output: False

