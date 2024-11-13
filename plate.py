from abc import ABC, abstractmethod

class Plate(ABC):
    """Interface for plates."""

    @abstractmethod
    def description(self):
        """:return: A string description of the plate and what is on it."""
        pass

    @abstractmethod
    def area(self):
        """:return: The remaining square inches the plate can hold."""
        pass

    @abstractmethod
    def weight(self):
        """:return: The remaining number of ounces the plate can hold."""
        pass

    @abstractmethod
    def count(self):
        """:return: The number of food items the plate is currently holding."""
        pass
