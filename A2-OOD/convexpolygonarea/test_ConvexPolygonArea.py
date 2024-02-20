#! /usr/bin/env python3

"""
Unit tests for convexpolygonarea.py
"""

import unittest
from convexpolygonarea import ConvexPolygonArea


class TestConvexPolygonArea(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = ConvexPolygonArea()

    def test_process_input(self) -> None:
        given_input = "4 0 0 4 0 4 4 0 4"
        expected_area = 16
        calculated_area = self.solver.process_input(given_input)
        self.assertEqual(calculated_area, expected_area)

    def test_process_input2(self) -> None:
        given_input = "4 1 -1 -1 -1 -1 1 1 1"
        expected_area = 4
        calculated_area = self.solver.process_input(given_input)
        self.assertEqual(calculated_area, expected_area)

    def test_process_input3(self) -> None:
        given_input = "3 -12 -2 -1 -14 -5 -7"
        expected_area = 14.5
        calculated_are = self.solver.process_input(given_input)
        self.assertEqual(calculated_are, expected_area)


if __name__ == '__main__':
    unittest.main()
