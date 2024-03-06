#! /usr/bin/env python3

"""
Convert input to a representation of morse code
"""

from typing import List


class convert_to_morse_code:
    """ Class to convert to morse code.
    . is represented with 1
    - is represented with 0 """
    _MORSE_LETTERS_DICT = {
        'A': (2, 1, 0),  # a -> .-
        'B': (4, 0, 1, 1, 1),  # b -> -...
        'C': (4, 0, 1, 0, 1),  # c -> -.-.
        'D': (3, 0, 1, 1),  # d -> -..
        'E': (1, 1),  # e -> .
        'F': (4, 1, 1, 0, 1),  # f -> ..-.
        'G': (3, 0, 0, 1),  # g -> --.
        'H': (4, 1, 1, 1, 1),  # h -> ....
        'I': (2, 1, 1),  # i -> ..
        'J': (4, 1, 0, 0, 0),  # j -> .---
        'K': (3, 0, 1, 0),  # k -> -.-
        'L': (4, 1, 0, 1, 1),  # l -> .-..
        'M': (2, 0, 0),  # m -> --
        'N': (2, 0, 1),  # n -> -.
        'O': (3, 0, 0, 0),  # o -> ---
        'P': (4, 1, 0, 0, 1),  # p -> .--.
        'Q': (4, 0, 0, 1, 0),  # q -> --.-
        'R': (3, 1, 0, 1),  # r -> .-.
        'S': (3, 1, 1, 1),  # s -> ...
        'T': (1, 0),  # t -> -
        'U': (3, 1, 1, 0),  # u -> ..-
        'V': (4, 1, 1, 1, 0),  # v -> ...-
        'W': (3, 1, 0, 0),  # w -> .--
        'X': (4, 0, 1, 1, 0),  # x -> -..-
        'Y': (4, 0, 1, 0, 0),  # y -> -.--
        'Z': (4, 0, 0, 1, 1),  # z -> --..
        '0': (5, 0, 0, 0, 0, 0),  # 0 -> -----
        '1': (5, 1, 0, 0, 0, 0),  # 1 -> .----
        '2': (5, 1, 1, 0, 0, 0),  # 2 -> ..---
        '3': (5, 1, 1, 1, 0, 0),  # 3 -> ...--
        '4': (5, 1, 1, 1, 1, 0),  # 4 -> ....-
        '5': (5, 1, 1, 1, 1, 1),  # 5 -> .....
        '6': (5, 0, 1, 1, 1, 1),  # 6 -> -....
        '7': (5, 0, 0, 1, 1, 1),  # 7 -> --...
        '8': (5, 0, 0, 0, 1, 1),  # 8 -> ---..
        '9': (5, 0, 0, 0, 0, 1)   # 9 -> ----.
    }

    @staticmethod
    def to_morse_code(text: str) -> List[int]:
        """ Converts a string to Morse code tuple representation
        using the MORSE_LETTERS_DICT """
        morse_code: List[int] = []
        for letter in text:
            if letter in convert_to_morse_code._MORSE_LETTERS_DICT:
                # add everything but the first element
                morse_code.extend(convert_to_morse_code.
                                  _MORSE_LETTERS_DICT[letter][1:])
            else:
                raise ValueError(f"Character '{letter}' is not allowed. ")
        return morse_code
