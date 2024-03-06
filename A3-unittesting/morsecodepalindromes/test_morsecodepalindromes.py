#! /usr/bin/env python3

"""
Unit tests for morsecodepalindromes.py
"""

import unittest
from hypothesis import given, strategies as st
from hypothesis.strategies import text
from morsecodepalindromes import morsecodepalindromes


class Testmorsecodepalindromes(unittest.TestCase):
    """ Class to test that the
    morsecodepalindromes class works as intended """
    def setUp(self) -> None:
        """ setUp function for creating instance """
        self.solver = morsecodepalindromes()

    @given(text(alphabet=st.characters(min_codepoint=48, max_codepoint=57) |
                st.characters(min_codepoint=65, max_codepoint=90) |
                st.characters(min_codepoint=97,
                              max_codepoint=122), max_size=80))
    def test_process_input(self, s: str) -> None:
        """ Test with valid input """
        result = self.solver.process_input(s)
        expected = ''.join(char.upper() for char in s if char.isalnum())
        self.assertEqual(result, expected)

    @given(st.text(min_size=81))
    def test_long_input(self, s: str) -> None:
        """ Test with input that is too long. """
        with self.assertRaises(ValueError):
            self.solver.process_input(s)
