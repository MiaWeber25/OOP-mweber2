#! /usr/bin/env python3
"""
This Module defines a class called ConvexPolygonArea
 that calculates the area of a convex polygon

This website was helpful for the math to calculate the area:
    https://www.mathwords.com/a/area_convex_polygon.htm
"""
from Point import Point
from Polygon import Polygon


class ConvexPolygonArea:
    """
    Calculates the area of a convex Polygon
        given the number of points followed
        by the x,y coordinates of each point
    """
    def __init__(self) -> None:
        """ No initialization required """
        pass

    def process_input(self, initial_input: str) -> float:
        """ Handed input and processes it to hand to appropriate functions """
        # split input into a list of strings (convert to int)
        user_input = list(map(int, initial_input.split()))
        num_points = user_input[0]  # number of points is first number
        new_polygon = Polygon(num_points)  # initialize the polygon

        # loop through the coordinates (in pairs)
        for i in range(1, 2 * num_points + 1, 2):
            x, y = user_input[i], user_input[i + 1]
            # add each coordinate pair to the polygon initialized above
            new_polygon.add_point(Point(x, y))

        return (new_polygon.find_area())

    def solve(self) -> None:
        """ solve() function gets input from user and calls
        appropriate methods to calculate area """
        n = int(input())
        for _ in range(n):
            initial_input = input()
            area = self.process_input(initial_input)

            # If the area is a whole number print it as an Integer
            formatted_area = int(area) if area.is_integer() else area
            print(formatted_area)
        # print(new_polygon.find_area())


if __name__ == "__main__":
    solved = ConvexPolygonArea()
    solved.solve()
