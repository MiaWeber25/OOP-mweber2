""" Module to test statistics.py """
import unittest
from typing import List
from hypothesis import given, strategies as st
from data_set import DataSet
from statistics import Statistics
from unittest.mock import patch, MagicMock


class TestStatistics(unittest.TestCase):
    """ Class to test the Statistics module. """
    @given(st.lists(st.integers(), min_size=1), st.integers(min_value=1))
    def test_solve(self, lst: List[int], case_num: int) -> None:
        """ Test solve """
        data_set = DataSet(lst)
        data_set.case_number = case_num
        expected_output = (
            f"Case {case_num}: "
            f"{min(lst)} {max(lst)} "
            f"{max(lst) - min(lst)}"
        )
        self.assertEqual(Statistics.solve(data_set), expected_output)

    @given(st.lists(st.integers(), min_size=2), st.integers(min_value=1))
    def test_process_data(self, input_data: List[int],
                          case_number: int) -> None:
        """ Test process_data """
        formatted_input = [len(input_data)] + input_data
        output = Statistics.process_data(formatted_input, case_number)
        expected_output = (
            f"Case {case_number}: "
            f"{min(input_data)} {max(input_data)} "
            f"{max(input_data) - min(input_data)}"
        )
        self.assertEqual(output, expected_output)

    @given(st.lists(st.integers()))
    def test_read_input(self, input_list: List[int]) -> None:
        """ Test read_input """
        input_string = ' '.join(map(str, input_list))  # Convert ints to string

        with patch('builtins.input', return_value=input_string):
            result = Statistics.read_input()
            self.assertEqual(result, input_list)

    @given(st.text())
    def test_print_output(eslf, test_output: str) -> None:
        """ Test print_output """
        with patch('builtins.print') as mock_print:
            Statistics.print_output(test_output)
            mock_print.assert_called_once_with(test_output)

    @patch('statistics.Statistics.print_output')
    @patch('statistics.Statistics.process_data', return_value='sample_output')
    @patch('statistics.Statistics.read_input',
           side_effect=[[4, 10, 20], [5, 1, 2, 3], EOFError])
    def test_process_input(self, sample_read_input: MagicMock,
                           sample_process_data: MagicMock,
                           sample_print_output: MagicMock) -> None:
        """ Test process_input """
        Statistics.process_input()

        self.assertEqual(sample_read_input.call_count, 3)  # 2+EOFError
        self.assertEqual(sample_process_data.call_count, 2)  # Called twice
        self.assertEqual(sample_print_output.call_count, 2)  # Called twice

        sample_print_output.assert_called_with('sample_output')


if __name__ == '__main__':
    unittest.main()
