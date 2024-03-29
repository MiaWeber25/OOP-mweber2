#! /usr/bin/env python3
"""
Module to test the code in weatherAPP.py
"""
import unittest
from weatherApp import WeatherApp

from hypothesis.strategies import integers
from hypothesis import given


class TestWeatherApp(unittest.TestCase):
    """ Class to test weatherApp.py """
    def setUp(self) -> None:
        """ set up functions """
        self.app = WeatherApp().app
        self.client = self.app.test_client()

    @given(integers(min_value=0))
    def test_date_filter(self, test_timestamp: float) -> None:
        """ test the date construction """
        test_timestamp = 0
        expected_date_str = "1970-01-01"

        date_filter = self.app.jinja_env.filters['date']

        result_date_str = date_filter(test_timestamp)

        # self.assertEqual(result_date_str, expected_date_str)
        assert result_date_str == expected_date_str
