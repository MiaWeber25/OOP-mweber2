#! /usr/bin/env python3

"""
Unit tests for Point.py
"""

import unittest
from Point import Point


class TestPoint(unittest.TestCase):
    def test_getter(self) -> None:
        point = Point(1, 2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_getter2(self) -> None:
        point = Point(-2, -2)
        self.assertEqual(point.x, -2)
        self.assertEqual(point.y, -2)

    def test_getter3(self) -> None:
        point = Point(-5, 5)
        self.assertEqual(point.x, -5)
        self.assertEqual(point.y, 5)

    def test_setter(self) -> None:
        point = Point(-1, 4)
        point.x = 4
        point.y = -1
        self.assertEqual(point.x, 4)
        self.assertEqual(point.y, -1)

    def test_setter2(self) -> None:
        point = Point(-4, -4)
        point.x = -8
        point.y = -5
        self.assertEqual(point.x, -8)
        self.assertEqual(point.y, -5)

    def test_setter3(self) -> None:
        point = Point(9, -9)
        self.assertEqual(point.x, 9)
        self.assertEqual(point.y, -9)


if __name__ == '__main__':
    unittest.main()
