"""
Module to test CupSequence
"""
import unittest
from typing import List, Tuple
from hypothesis import given, strategies as st
from cup_sequence import CupSequence


class TestCupSequence(unittest.TestCase):

    def initial_length(self) -> None:
        c: CupSequence = CupSequence()
        self.assertEqual(len(c), 0, "Initial sequence should be empty")

    @given(st.lists(st.tuples(st.integers(
            min_value=1, max_value=100), st.text(
                min_size=1, max_size=10)), unique=True))
    def test_sequence_operations(
        self, input_list: List[Tuple[
            int, str]]) -> None:
        c: CupSequence = CupSequence()

        # Test inserting data
        for item in input_list:
            c.append(item)
        self.assertEqual(len(c), len(
            input_list), "Length of sequence should match length of items")

        # Test __getitem__ and __setitem__
        for i, item in enumerate(input_list):
            self.assertEqual(
                c[i], item, "item should be the same as original item")
            new_item: tuple[int, str] = (item[0] + 1, item[1] + 'x')
            c[i] = new_item
            self.assertEqual(
                c[i], new_item, "Item should get updated as intended")

        # Test sorting
        c.sort_cups()
        sorted_input: List[Tuple[
            int, str]] = sorted(
                input_list, key=lambda x: x[0])
        for i, item in enumerate(sorted_input):
            self.assertEqual(c[i], (
                item[0] + 1, item[1] + 'x'), "Items are sorted by radius")

    @given(st.lists(
            st.tuples(st.integers(), st.text(
                min_size=1)), min_size=2, unique=True))
    def test_deletion(self, input_list: List[Tuple[int, str]]) -> None:
        """ Test deletion effects. """
        c: CupSequence = CupSequence()
        for item in input_list:
            c.append(item)
        original_sequence: List[Tuple[int, str]] = list(c)

        del c[0]
        self.assertNotEqual(
            c[0], original_sequence[0], "First item should be del")
        self.assertEqual(len(c), len(input_list) - 1, "Length decrease by one")

        for i in range(1, len(input_list)):
            self.assertEqual(
                c[i-1], original_sequence[i],
                "Remaining items should be unchanged")

    @given(initial_items=st.lists(
            st.tuples(st.integers(), st.text()), unique=True),
           new_item=st.tuples(st.integers(), st.text()),
           index=st.integers(min_value=0))
    def test_insert(
        self, initial_items: List[
            Tuple[int, str]], new_item: Tuple[
                int, str], index: int) -> None:
        c: CupSequence = CupSequence()
        for item in initial_items:
            c.append(item)
        # Wrap index around to valid range
        index = index % (len(c) + 1)
        c.insert(index, new_item)

        # Check location of new_item:
        self.assertEqual(c[index], new_item, f"New item should be at: {index}")
        # Check length:
        self.assertEqual(len(c), len(
            initial_items) + 1, "Len of sequence should incrememt")

    def test_slice_retrieval(self) -> None:
        """ Can return a CupSequence? """
        c = CupSequence()
        items = [(i, str(i)) for i in range(10)]
        for item in items:
            c.append(item)

        start, stop, step = 1, 7, 2
        sliced_cup_sequence = c[start:stop:step]

        self.assertIsInstance(
            sliced_cup_sequence, CupSequence,
            "Should return CupSequence")

    """ Test with explicit instances for ValueErrors. """
    def test_setitem_invalid_index(self) -> None:
        """ Test setitem with invalid index. """
        c = CupSequence()
        c.append((1, 'red'))
        with self.assertRaises(ValueError):
            c[0] = [2, 'blue']  # type: ignore[call-overload]

    def test_setitem_valid_slice(self) -> None:
        """ Test setitem with iterable slice. """
        c = CupSequence()
        c.extend([(1, 'red'), (2, 'blue')])
        c[0:2] = [(3, 'green'), (4, 'yellow')]  # Valid iterable of tuples
        self.assertEqual(c[0], (
            3, 'green'), "First item should be updated correctly")
        self.assertEqual(c[1], (
            4, 'yellow'), "Second item should be updated correctly")

    def test_setitem_non_iterable(self) -> None:
        """ Test setitem with non-iterable index. """
        c = CupSequence()
        c.extend([(1, 'red'), (2, 'blue')])
        with self.assertRaises(TypeError):
            c[0:1] = None  # type: ignore[call-overload]

    def test_setitem_invalid_index2(self) -> None:
        """ Test setitem with invalid index. """
        c = CupSequence()
        c.extend([(1, 'red'), (2, 'blue')])
        with self.assertRaises(TypeError):
            c['invalid'] = (3, 'green')  # type: ignore[call-overload]


if __name__ == '__main__':
    unittest.main()
