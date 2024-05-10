"""
Module to test CupStacking
"""
import unittest
from hypothesis import given, strategies as st
from unittest.mock import patch, MagicMock
from typing import List, Tuple
from cup_stacking import CupStacking
import io


class TestCupStacking(unittest.TestCase):

    # def mock_input(self, data: List[str]) -> Generator[str, None, None]:
    def mock_input(self, data: List[str]) -> io.StringIO:
        """ Function to mock the input. """
        input_str = "\n".join(data)
        return io.StringIO(input_str)
        # for item in data:
        #   yield item

    @given(
        st.lists(
            st.tuples(
                st.text(
                    min_size=1,
                    alphabet=st.characters(whitelist_categories=['Ll', 'Lu'])
                ),
                st.integers(min_value=1, max_value=100)
            ),
            unique=True,
            min_size=1,
            max_size=100
        )
    )
    def test_read_input(self, cups: List[Tuple[str, int]]) -> None:
        """ Test ability to read input correctly. """
        input_data = ["{} {}".format(cup[0], cup[1]) for cup in cups]
        input_data.insert(0, str(len(cups)))

        input_source = self.mock_input(input_data)

        # Instantiate CupStacking with mocked input source
        c = CupStacking(input_source)
        try:
            c.read_input()

            print(f"Expected number of cups: {len(cups)}")
            print(f"Actual number of cups: {len(c.data)}")
            for cup in c.data:
                print(f"Cup: Radius={cup[0]}, Color={cup[1]}")
        # print(f"Cup data: {list(c.data)}")
            self.assertEqual(
                len(c.data),
                len(cups),
                f"Expected {len(cups)}, but got {len(c.data)}")
        except ValueError as e:
            self.fail(f"Failed to read input correctly with error: {e}")

    @given(
        st.lists(
            st.one_of(
                st.tuples(
                    st.integers(min_value=2, max_value=100).map(
                        lambda x: str(x * 2)),
                    st.text(min_size=1, max_size=10,
                            alphabet=st.characters(
                                whitelist_categories=['Ll', 'Lu']))
                ),
                st.tuples(
                    st.text(min_size=1, max_size=10,
                            alphabet=st.characters(
                                whitelist_categories=['Ll', 'Lu'])),
                    st.integers(min_value=1, max_value=50).map(str)
                )
            ),
            unique=True, min_size=1, max_size=10
        )
    )
    def test_read_input2(self, cups: List[Tuple[str, str]]) -> None:
        input_data = ["{} {}".format(*cup) for cup in cups]
        input_data.insert(0, str(len(input_data)))
        # input_data = [str(len(input_data))] + input_data
        input_source = self.mock_input(input_data)
        c = CupStacking(input_source)
        c.read_input()
        self.assertEqual(len(c.data), len(cups))

    @given(st.lists(st.tuples(
        st.integers(min_value=1, max_value=100),
        st.text(
            min_size=1, max_size=10, alphabet=st.characters(
                whitelist_categories=['Lu', 'Ll']))
        ), unique_by=lambda x: x[0], min_size=1, max_size=20))
    def test_solve(self, input_list: List[Tuple[int, str]]) -> None:
        """ Test sort solving method. """
        mock_import = MagicMock()
        c = CupStacking(mock_import)

        c._data.extend(input_list)
        c.solve()

        sorted_by_radius = sorted(input_list, key=lambda x: x[0])
        self.assertEqual(
            [cup for cup in c.data],
            sorted_by_radius, "Cups should be sorted.")

    @given(
        st.lists(
            st.tuples(
                st.integers(min_value=1, max_value=100),
                st.text(min_size=1, max_size=10)
            ),
            unique_by=lambda x: x[1], min_size=1, max_size=20
        )
    )
    def test_answer_sorted(self, cups: List[Tuple[int, str]]) -> None:
        """ Did it sort things correctly? """
        blank_input = io.StringIO("")
        c = CupStacking(blank_input)
        c._data.extend(cups)
        c._data.sort_cups()

        expected_colors_sorted = [
            color for _, color in sorted(
                cups, key=lambda x: x[0])]
        actual_colors = c.answer

        self.assertEqual(
            actual_colors, expected_colors_sorted, "Colors should be sorted.")

    @given(
        st.lists(
            st.tuples(
                st.integers(min_value=1, max_value=100),
                st.text(min_size=1, max_size=10)
            ),
            unique_by=lambda x: x[1], min_size=1, max_size=20
        )
    )
    def test_print_answer(self, cups: List[Tuple[int, str]]) -> None:
        """ Test answer printing logic. """
        blank_input = io.StringIO("")
        c = CupStacking(blank_input)
        c._data.extend(cups)
        c._data.sort_cups()

        expected = "\n".join(
            color for _, color in sorted(
                cups, key=lambda x: x[0])) + '\n'

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            c.print_answer()
            self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
