from abc import ABC
from plate import Plate

class PlateDecorator(Plate, ABC):
    """ Abstract base class for a decorator that adds food to a plate and changes the plate's properties as food is added.

    Attributes:
        _plate: :class:`Plate` attribute to represent a plate with food on it.
    """

    def __init__(self, p: Plate):
        """Constructor for :class:`PlateDecorator`.

        :param p: :class:`Plate` attribute to represent the previous state of the plate.
        """
        self._plate = p

    def description(self) -> str:
        """:return: The description of :attr:`self._plate`."""
        return self._plate.description()

    def area(self) -> int:
        """:return: The area of :attr:`self._plate`."""
        return self._plate.area()

    def weight(self) -> int:
        """:return: The weight capacity of :attr:`self._plate`."""
        return self._plate.weight()

    def count(self) -> int:
        """:return: The number of food items on :attr:`self._plate`."""
        return self._plate.count()