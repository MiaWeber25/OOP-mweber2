#! /usr/bin/env python3

"""
Unit tests for convert_to_morse_code.py
"""

from hypothesis import given, strategies as st
from convert_to_morse_code import convert_to_morse_code
import unittest


class Test_convert_to_morse_code(unittest.TestCase):
    """ Class to test that the
    convert_to_morse_code class works as intended """
    @given(st.text(alphabet=list(convert_to_morse_code
                                 ._MORSE_LETTERS_DICT.keys())))
    def test_to_morse_code_valid(self, text: str) -> None:
        """ test with valid input"""
        try:
            code = convert_to_morse_code.to_morse_code(text)
            self.assertIsInstance(code, list)
            self.assertTrue(all(isinstance(code, int) for code in code))
        except ValueError:
            self.fail()

    @given(st.text(min_size=1).filter(lambda x: any
                                      (c not in convert_to_morse_code
                                       ._MORSE_LETTERS_DICT for c in x)))
    def test_to_morse_code_invalid(self, text: str) -> None:
        """ test with invalid input.
        Use the lambda function in .filter() to ensure string x has at
        least one char not in List """
        with self.assertRaises(ValueError):
            convert_to_morse_code.to_morse_code(text)
