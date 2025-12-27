
# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstract methods



# ABC = Abstract Base Class
#
# It’s used to create a blueprint for other classes
#
# abstractmethod forces child classes to implement certain methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# vehicle = Vehicle()
#
#     vehicle = Vehicle()
# TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'
#

