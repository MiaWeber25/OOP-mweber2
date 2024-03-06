#! /usr/bin/env python3
"""
This module defines a class called morsecodepalindromes
that determines if a string is a morse code palindrome.

This code was helpful to reference:
https://github.com/justinsight/MorsePalindromeFinder/blob/main/PalindromeFinder.java
"""

from convert_to_morse_code import convert_to_morse_code
from palindrome_checker import palindrome_checker


class morsecodepalindromes:
    """
    Determines if a given string is a morse code palindrome.
    Outputs a "1" if it is and a "0" otherwise.
    """
    def __init__(self) -> None:
        """ No initialization required """
        pass

    def process_input(self, text: str) -> str:
        """ Removes unwanted chars and converts to uppercase
        ensures the text is <= 80 chars """
        if len(text) > 80:
            raise ValueError("Input longer than 80 chars.")
        return ''.join(char.upper() for char in text if char.isalnum())

    def solve(self) -> None:
        """ solve() function gets input from user and calls
        appropriate methods to determine if a morse code
        palindrome is found """
        text = self.process_input(input())
        if not text:
            print('0')
            return
        encoded_text = convert_to_morse_code.to_morse_code(text)
        if palindrome_checker.is_palindrome(encoded_text):
            print('1')
        else:
            print('0')


if __name__ == "__main__":
    solved = morsecodepalindromes()
    solved.solve()
