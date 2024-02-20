#! /usr/bin/env python3

"""
Unit tests for Polygon.py
"""

import unittest
from Polygon import Polygon
from Point import Point


class TestPolygon(unittest.TestCase):

    def test_add_point(self) -> None:
        polygon = Polygon(3)
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(1, 0))
        polygon.add_point(Point(0, 1))
        self.assertEqual(len(polygon.points), 3)

    def test_add_point2(self) -> None:
        polygon = Polygon(4)
        polygon.add_point(Point(1, 40))
        polygon.add_point(Point(2, 3))
        polygon.add_point(Point(2, -7))
        polygon.add_point(Point(2, 10))
        self.assertEqual(len(polygon.points), 4)

    def test_add_point3(self) -> None:
        polygon = Polygon(8)
        polygon.add_point(Point(5, 40))
        polygon.add_point(Point(-1, 5))
        polygon.add_point(Point(1, -7))
        polygon.add_point(Point(3, 10))
        polygon.add_point(Point(9, 4))
        polygon.add_point(Point(6, 3))
        polygon.add_point(Point(-5, -7))
        polygon.add_point(Point(4, -4))
        self.assertEqual(len(polygon.points), 8)

    def test_valid_polygon(self) -> None:
        polygon = Polygon(3)
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(1, 0))
        self.assertFalse(polygon.valid_polygon())

    def test_valid_polygon2(self) -> None:
        polygon = Polygon(8)
        polygon.add_point(Point(5, 40))
        polygon.add_point(Point(-1, 5))
        polygon.add_point(Point(1, -7))
        polygon.add_point(Point(3, 10))
        polygon.add_point(Point(9, 4))
        polygon.add_point(Point(6, 3))
        polygon.add_point(Point(-5, -7))
        polygon.add_point(Point(4, -4))
        polygon.add_point(Point(-2, 3))
        self.assertFalse(polygon.valid_polygon())

    def test_valid_polygon3(self) -> None:
        polygon = Polygon(4)
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(3, 4))
        polygon.add_point(Point(8, 10))
        polygon.add_point(Point(-1, 4))
        self.assertTrue(polygon.valid_polygon())

    def test_find_area(self) -> None:
        polygon = Polygon(4)
        polygon.add_point(Point(1, 4))
        polygon.add_point(Point(3, 3))
        polygon.add_point(Point(2, -1))
        polygon.add_point(Point(5, 8))
        expected_area = 7.5
        self.assertEqual(expected_area, polygon.find_area())

    def test_find_area2(self) -> None:
        polygon = Polygon(8)
        polygon.add_point(Point(5, 40))
        polygon.add_point(Point(-1, 5))
        polygon.add_point(Point(1, -7))
        polygon.add_point(Point(3, 10))
        polygon.add_point(Point(9, 4))
        polygon.add_point(Point(6, 3))
        polygon.add_point(Point(-5, -7))
        polygon.add_point(Point(4, -4))
        expected_area = 112
        self.assertEqual(expected_area, polygon.find_area())

    def test_find_area3(self) -> None:
        polygon = Polygon(3)
        polygon.add_point(Point(-12, -2))
        polygon.add_point(Point(-1, -14))
        polygon.add_point(Point(-5, -7))
        expected_area = 14.5
        self.assertEqual(expected_area, polygon.find_area())

    def test_num_points_getter(self) -> None:
        polygon = Polygon(3)
        self.assertEqual(polygon.num_points, 3)

    def test_num_points_getter2(self) -> None:
        polygon = Polygon(14)
        self.assertEqual(polygon.num_points, 14)

    def test_num_points_getter3(self) -> None:
        polygon = Polygon(6)
        self.assertEqual(polygon.num_points, 6)

    def test_num_points_setter(self) -> None:
        polygon = Polygon(3)
        polygon.num_points = 6
        self.assertEqual(polygon.num_points, 6)

    def test_num_points_setter2(self) -> None:
        polygon = Polygon(7)
        polygon.num_points = 7
        self.assertEqual(polygon.num_points, 7)

    def test_num_points_setter3(self) -> None:
        polygon = Polygon(15)
        polygon.num_points = 145
        self.assertEqual(polygon.num_points, 145)

    def test_points_getter(self) -> None:
        polygon = Polygon(4)
        polygon.add_point(Point(-4, 3))
        polygon.add_point(Point(6, -6))
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(1, -1))
        points_copy = polygon.points
        self.assertEqual(len(points_copy), 4)

    def test_points_getter2(self) -> None:
        polygon = Polygon(3)
        polygon.add_point(Point(-12, 0))
        polygon.add_point(Point(-56, 6))
        polygon.add_point(Point(1, -12))
        points_copy = polygon.points
        self.assertEqual(len(points_copy), 3)

    def test_points_getter3(self) -> None:
        polygon = Polygon(5)
        polygon.add_point(Point(-23, 9))
        polygon.add_point(Point(-6, 12))
        polygon.add_point(Point(92, -5))
        polygon.add_point(Point(-56, 12))
        polygon.add_point(Point(-7, 7))
        points_copy = polygon.points
        self.assertEqual(len(points_copy), 5)


if __name__ == '__main__':
    unittest.main()
