""" Module to test statistics.py """
import unittest
from hypothesis import given, strategies as st
from data_set import DataSet
from statistics import Statistics
from unittest.mock import patch

class TestStatistics(unittest.TestCase):
    """ Class to test the Statistics module. """
    @given(st.lists(st.integers(), min_size=1), st.integers(min_value=1))
    def test_solve(self, lst, case_num):
        """ Test solve """
        data_set = DataSet(lst)
        data_set.case_number = case_num
        expected_output = f"Case {case_num}: {min(lst)} {max(lst)} {max(lst) - min(lst)}"
        self.assertEqual(Statistics.solve(data_set), expected_output)

    """@patch('builtins.input', side_effect=['4 10 20 30 40', '5 1 2 3 4 5', EOFError])
    def test_process_input(self, mock_input):
        with self.assertRaises(EOFError):
            Statistics.process_input()
            self.assertEqual(mock_input.call_count, 3)"""
    
    @patch('builtins.input')
    def test_process_input(self, mock_input):
        # Correct side_effect: After two inputs, EOFError will be raised on the third call.
        mock_input.side_effect = ['4 10 20 30 40', '5 1 2 3 4 5', EOFError]

        # We don't need to catch EOFError in a try-except block since it's expected behavior here.
        with self.assertRaises(EOFError):
            Statistics.process_input()

        # The assertion should now expect the mock_input to have been called exactly three times:
        # Twice for the input data and once to trigger the EOFError.
        self.assertEqual(mock_input.call_count, 3)

if __name__ == '__main__':
    unittest.main()