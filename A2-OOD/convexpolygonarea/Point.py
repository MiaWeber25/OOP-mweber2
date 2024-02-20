"""
This module defines a class and methods for
defining a point in space and accessing the point
"""


class Point:
    """ Represents a single point in 2D space.
    Attributes:
    x (float) - the x coordinate of a Point
    y (float) - the y coordinate of a Point
    """

    def __init__(self, x: float, y: float) -> None:
        """ Initialize a Point with x,y coordinates
        Parameters:
        x (float) - the x coordinate of a Point
        y (float) - the y coordinate of a Point
        """
        self._x: float = x
        self._y: float = y

    @property
    def x(self) -> float:
        """ Getter for the x coordinate """
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """ Setter for the x coordinate """
        self._x = value

    @property
    def y(self) -> float:
        """ Getter for the y coordinate """
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """ Setter for the y coordinate """
        self._y = value
