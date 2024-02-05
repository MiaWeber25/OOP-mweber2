#! /usr/bin/env python3

"""
Unit tests for solution.py
"""

import unittest

from sorttwonumbers import sort


class TestSort(unittest.TestCase):
    def test1(self) -> None:
        self.assertFalse(sort(8, 2))

    def test2(self) -> None:
        self.assertTrue(sort(-4, 4))

    def test3(self) -> None:
        self.assertFalse(sort(-7485, -7485))


if __name__ == "__main__":
    unittest.main()
