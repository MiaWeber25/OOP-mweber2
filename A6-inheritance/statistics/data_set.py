"""
This module contains logic to calculate min, max, and range.
"""
from typing import Iterable, Any


class DataSet(list[int]):
    """ Class Data_Set inherits from built-in List Class """

    def __init__(self, iterable: Iterable[Any]) -> None:
        """ Initialize case_number and override init. """
        super().__init__(iterable)
        self._case_number: int = 0

    @property
    def case_number(self) -> int:
        """ Getter for case_number. """
        return self._case_number

    @case_number.setter
    def case_number(self, value: int) -> None:
        """ Setter for case_number with validation. """
        if not isinstance(value, int) or value < 1:
            raise ValueError("case_number must be a positive integer")
        self._case_number = value

    def get_min(self) -> Any:
        """ Method to calculate min value for elements. """
        return min(self)

    def get_max(self) -> Any:
        """ Method to calculate max value for elements. """
        return max(self)

    def get_range(self) -> Any:
        """ Method to calculate range for elements. """
        return self.get_max() - self.get_min()
