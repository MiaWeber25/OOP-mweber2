"""
CupSequence is derived from collections.abc.MutableSequence
Correctly overrides __len__(), __getitem__(index), __setitem__(index, value),
__delitem__(index), insert(index, value) & adds the method sort_cups().
"""
from collections.abc import MutableSequence
from typing import Tuple, List, Union, Iterable, overload


class CupSequence(MutableSequence[Tuple[int, str]]):
    """
    Mutable sequence to store cup data - tuple of (radius, color)
    """
    def __init__(self) -> None:
        """ Initialize the list of cups. """
        self._cups: List[Tuple[int, str]] = []

    def __len__(self) -> int:
        """ Get the length of the sequence. """
        return len(self._cups)

    # Had to add others to pass mypy
    @overload
    def __getitem__(self, index: int) -> Tuple[int, str]: ...

    @overload
    def __getitem__(self, s: slice) -> 'CupSequence': ...

    def __getitem__(self, index: Union[
        int, slice]) -> Union[Tuple[
            int, str], 'CupSequence']:
        if isinstance(index, slice):
            new_cup_seq = CupSequence()
            new_cup_seq._cups = self._cups[index]
            return new_cup_seq
        return self._cups[index]

    # @overload
    # def __getitem__(self, index: int) -> Tuple[int, str]:
        """ Get an item. """
    # return self._cups[index]

    @overload
    def __setitem__(self, index: int, value: Tuple[int, str]) -> None: ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[
        Tuple[int, str]]) -> None: ...

    def __setitem__(self, index: Union[
        int, slice], value: Union[
            Tuple[int, str], Iterable[
                Tuple[int, str]]]) -> None:
        """ Set the (radius, color) of an item. """
        # self._cups[index] = value
        if isinstance(index, int):
            if not isinstance(value, tuple):
                raise ValueError(
                    "Expected a tuple for integer index assignment")
            self._cups[index] = value
        elif isinstance(index, slice):
            if not isinstance(value, Iterable) or isinstance(value, tuple):
                raise TypeError("Expected an interable of tuples")
            self._cups[index] = list(value)
        else:
            raise TypeError("Index must be an int or slice")

    # @overload
    # def __setitem__(self, index: int, value: Tuple[int, str]) -> None:
    #   """ Set the (radius, color) of an item. """
    #  self._cups[index] = value

    @overload
    def __delitem__(self, index: int) -> None: ...

    @overload
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index: Union[int, slice]) -> None:
        """ Delete an item. """
        del self._cups[index]

    # @overload
    # def __delitem__(self, index: int) -> None:
        """ Delete an item. """
    #   del self._cups[index]

    def insert(self, index: int, value: Tuple[int, str]) -> None:
        """ Insert an item w/ index and (radius, color). """
        self._cups.insert(index, value)

    def sort_cups(self) -> None:
        """ Sort the cups based on their radius. """
        self._cups.sort(key=lambda cup: cup[0])
