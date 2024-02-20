"""
This module defines a class a methods for defining a Polygon,
    adding Points to the Polygon, checking if it's a valid Polygon,
    and calculating the area of the Polygon
"""
from Point import Point
from typing import List


class Polygon:
    """ Represents a convex polygon in 2D space.
    Attributes:
    points (List[Point]) - a Polygon is an array of Points
    num_points (int) - a count of the total Points
    """
    def __init__(self, num_points: int) -> None:
        """ Initialize a Polygon with an empty array for the
        points and a count of the total points
        Parameters:
        num_points (int) - a count of the total Points
        """
        self._points: List[Point] = []  # a polygon is a List of Points
        self._num_points: int = num_points  # count of the total points

    def add_point(self, point: Point) -> None:
        """ Add a Point to the Polygon.
        Checks to make sure that that point does
        not exceed the expected count of points.

        Parameters:
        point (Point) - the Point to add to the Polygon

        Raises:
        ValueError: If adding the point is out of bounds.
        """
        # Check to make sure points entered are in bounds
        if len(self._points) <= self._num_points:
            self._points.append(point)  # add a point to the array
        else:
            raise ValueError("Can't add more points then promised")

    def valid_polygon(self) -> bool:
        """ Check to see if the actual points
        entered matches expected number of points """
        return len(self._points) == self._num_points

    @property
    def num_points(self) -> int:
        """ Getter for num_points """
        return self._num_points

    @num_points.setter
    def num_points(self, value: int) -> None:
        """ Setter for num_points """
        self._num_points = value

    @property
    def points(self) -> List[Point]:
        """ Getter for points. To prevent modification
        of the List, returns a shallow copy """
        return self._points[:]

    def find_area(self) -> float:
        """ Find the area of the convex polygon """
        area = 0.0  # initalize the area to 0 (float)
        n = len(self._points)  # n is how many points are in the polygon
        for i in range(n):
            j = (i + 1) % n  # next coordinates
            area += self._points[i].x * self._points[j].y
            area -= self._points[j].x * self._points[i].y
        return abs(area / 2.0)
