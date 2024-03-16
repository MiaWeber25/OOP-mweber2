#! /usr/bin/env python3
""" This module contains unit tests for calc_cost.py """

import unittest
from hypothesis import given, strategies as st
from calc_cost import calc_cost


class test_calc_cost(unittest.TestCase):
    """ tests for modules in calc_cost """
    @given(st.text())
    def test_calculate_cost(self, title: str) -> None:
        """ test functionality of calculate_cost """
        cost = calc_cost.calculate_cost(title)
        self.assertEqual(cost, len(title))
