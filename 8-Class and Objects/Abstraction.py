'''
Definition:
Abstraction is the process of hiding complex implementation details and only showing essential features to the user.

🔹 Example:
Think of a car:

You only need to press the accelerator to move forward.

You don’t need to know how the engine, fuel injection, or transmission works
'''

from abc import ABC, abstractmethod  # Importing ABC module

# Abstract class
class Vehicle(ABC):  
    @abstractmethod
    def start(self):
        """Abstract method (must be implemented by subclasses)"""
        pass

# Concrete subclass
class Car(Vehicle):
    def start(self):
        print("Car engine started!")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started!")

# Creating objects
car = Car()
car.start()  # Output: Car engine started!

bike = Bike()
bike.start()  # Output: Bike engine started!
