"""
Class that is derived from the provided Kattis ABC class.
Correctly overrides read_input(self), solve(self), and print_answer(self).
"""
from typing import TextIO, List
from kattis_base import Kattis
from cup_sequence import CupSequence


class CupStacking(Kattis):
    """ Class to solve the "Stacking Cups" problem in Kattis. """
    def __init__(self, data_source: TextIO) -> None:
        """ Intialize the data. """
        super().__init__(data_source)
        self._data: CupSequence = CupSequence()

    def read_input(self) -> None:
        """
        Override abstract method to read input
        num of entries & each entry (color and size (rad or diam ))
        """
        n = int(next(self._input_source))
        for _ in range(n):
            line = next(self._input_source).strip().split()
            if line[0].isdigit():
                radius = int(line[0]) // 2  # number is first = radius/2
                color = line[1]  # second param = color
            else:
                color = line[0]  # first param = color
                radius = int(line[1])  # radius = second param
            self._data.append((radius, color))

    @property
    def data(self) -> CupSequence:
        """ Return the internal data storing cups. """
        return self._data

    @property
    def answer(self) -> List[str]:
        """ Return list of cup colors - sorted. """
        return [cup[1] for cup in self._data]

    def solve(self) -> None:
        """ Sort cups based on radius. """
        self._data.sort_cups()

    def print_answer(self) -> None:
        """ Output cups in correct order (increasing size). """
        for _, color in self._data:
            print(color)
