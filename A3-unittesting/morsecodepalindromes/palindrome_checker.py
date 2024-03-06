#! /usr/bin/env python3

"""
Check to see if given input is a palindrome
"""

from typing import List


class palindrome_checker:
    """ Class to reverse input to see if input is a palindrome """
    @staticmethod
    def is_palindrome(encoded: List[int]) -> bool:
        """ Checks if the given encoded text is a palindrome
        checks if text is equal to text when reversed """
        return encoded == encoded[::-1]
