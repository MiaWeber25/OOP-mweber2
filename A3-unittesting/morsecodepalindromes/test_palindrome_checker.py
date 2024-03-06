#! /usr/bin/env python3

"""
Unit tests for palindrome_checker.py
"""

import unittest
from typing import List
from hypothesis import given, strategies as st
from palindrome_checker import palindrome_checker


class Test_palindrome_checker(unittest.TestCase):
    """ Class to test that the
    palindrome_checker class works as intended """
    @given(st.lists(st.integers(), min_size=1).map(lambda x: x + x[::-1]))
    def test_is_palindrome_palindromes(self, lst: List[int]) -> None:
        """ test with palindromes.
        Use st.lists(st.integers()) to generate list of ints and
          make sure it's palindrome by adding the reverse """
        self.assertTrue(palindrome_checker.is_palindrome(lst))

    @given(st.lists(st.integers(), min_size=2))
    def test_is_palindrome_non_palindromes(self, lst: List[int]) -> None:
        """ test with non-palindromes """
        lst.append(lst[0] + 1)  # make sure it's not a palindrome!
        self.assertFalse(palindrome_checker.is_palindrome(lst))
