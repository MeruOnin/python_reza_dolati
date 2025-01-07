from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def Move(self):
        """"please impotant method"""


c = Vehicle()

