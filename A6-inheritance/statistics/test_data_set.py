""" Module to test data_set.py """
import unittest
from hypothesis import given, strategies as st
from data_set import DataSet

class TestDataSet(unittest.TestCase):
    """ Class to test the DataSet module. """
    @given(st.lists(st.integers()))
    def test_init(self, lst):
        """ Test initialization. """
        data_set = DataSet(lst)
        self.assertEqual(list(data_set), lst)
    
    @given(st.integers(min_value=1))
    def test_case_number(self, case_num):
        """ Test setting and getting for case_number """
        data_set = DataSet([2, 6, 19])
        data_set.case_number = case_num
        self.assertEqual(data_set.case_number, case_num)
    
    @given(st.one_of(st.integers(max_value=0), st.text(), st.floats()))
    def test_case_number_validation(self, case_num):
        """ Test invalid case_number ValueError """
        data_set = DataSet([2, 6, 19])
        with self.assertRaises(ValueError):
            data_set.case_number = case_num

    @given(st.lists(st.integers(), min_size=1))
    def test_get_min(self, lst):
        """ Test get_min() """
        data_set = DataSet(lst)
        self.assertEqual(data_set.get_min(), min(lst))
    
    @given(st.lists(st.integers(), min_size=1))
    def test_get_max(self, lst):
        """ Test get_max() """
        data_set = DataSet(lst)
        self.assertEqual(data_set.get_max(), max(lst))
    
    @given(st.lists(st.integers(), min_size=1))
    def test_get_range(self, lst):
        """ Test get_range() """
        data_set = DataSet(lst)
        self.assertEqual(data_set.get_range(), max(lst) - min(lst))

if __name__ == "__main__":
    unittest.main()
