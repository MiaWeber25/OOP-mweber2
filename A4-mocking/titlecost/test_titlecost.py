#! /usr/bin/env python3
""" This module contains unit tests for titlecost.py """
import unittest
from hypothesis import given
import importlib.util
import importlib
import sys
import hypothesis.strategies as st
from unittest.mock import patch, Mock
from types import ModuleType
from io import StringIO
from titlecost import titlecost  # Adjust import path as necessary


class test_titlecost(unittest.TestCase):
    """ Class to test that the
    titlecost class works as intended """
    def test_init(self) -> None:
        """ Method to test the constructor of titlecost """
        instance = titlecost()
        self.assertIsInstance(instance, titlecost)

    #  @given(st.text(alphabet=st.characters(
        #  whitelist_categories=('Lu', 'Ll')),
        #  min_size=1, max_size=30))
    @given(st.text(alphabet=st.characters(min_codepoint=65, max_codepoint=90) |
                   st.characters(min_codepoint=97, max_codepoint=122),
                   min_size=1, max_size=30))
    def test_validate_title(self, title: str) -> None:
        """ Test with valid title """
        result = titlecost.validate_title(title)
        self.assertEqual(title, result)

    @given(st.text(min_size=0).filter(lambda x: not x.isalpha()
                                      or len(x) > 30))
    def test_validate_title_invalid(self, title: str) -> None:
        """ Test with invalid title """
        with self.assertRaises(ValueError):
            titlecost.validate_title(title)

    @given(st.floats(min_value=0, max_value=100))
    def test_validate_max_cost(self, max_cost: float) -> None:
        """ Test with valid max_cost (0-100)"""
        max_cost_str = str(max_cost)
        result = titlecost.validate_max_cost(max_cost_str)
        self.assertEqual(result, max_cost)

    @given(st.one_of(st.text(min_size=1).filter(lambda x:
                                                not x.replace('.', '', 1).
                                                isdigit()),
                     st.floats().filter(lambda x: x < 0 or x > 100)))
    def test_validate_max_cost_invalid(self, max_cost: float) -> None:
        """ Test with invalid max_cost (non-float strings & out-of-range) """
        with self.assertRaises(ValueError):
            str_max_cost = str(max_cost)
            titlecost.validate_max_cost(str_max_cost)

    @patch('sys.stdin', new_callable=lambda: StringIO('newMovie 10'))
    @patch('builtins.print')
    def test_solve(self, mock_print: Mock, mock_stdin: Mock) -> None:
        """ Test valid input """
        t = titlecost()
        t.solve()
        mock_print.assert_called_once_with(8.0)

    @patch('builtins.input', return_value='movieTitle 15')
    @patch('titlecost.calc_cost.calculate_cost', return_value=10)
    @patch('builtins.print')
    def test_solve2(self, mock_print: Mock, mock_calc_cost: Mock,
                    mock_input: Mock) -> None:
        """ test with mocked input and calc_cost (import guard) """
        t = titlecost()
        t.solve()
        mock_calc_cost.assert_called_once_with('movieTitle')
        mock_print.assert_called_once_with(10)

    def test_import_guard(self) -> None:
        """Test the if __name__ == '__main__': block of titlecost.py."""
        # Mock input and print functions
        with patch('builtins.input', return_value='movie 3'), \
            patch('builtins.print') as mock_print, \
                patch('titlecost.calc_cost.calculate_cost', return_value=3):
            # Construct a module
            spec = importlib.util.spec_from_file_location("__main__",
                                                          "titlecost.py")
            # Create a new module based on above
            if spec is not None and spec.loader is not None:
                module = importlib.util.module_from_spec(spec)
                assert isinstance(module, ModuleType)
            # Add the module to sys.modules
                sys.modules["__main__"] = module
            # Execute the module's code
                spec.loader.exec_module(module)
                mock_print.assert_called_once_with(3)
            else:
                self.fail()


if __name__ == "__main__":
    unittest.main()
