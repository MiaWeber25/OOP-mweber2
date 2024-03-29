#! /usr/bin/env python3
"""
Module to test the weatherAPI.py code
Helpful: https://realpython.com/testing-third-party-apis-with-mocks/
"""
from unittest.mock import patch, MagicMock
import unittest
from hypothesis import given, strategies as st, settings
from weatherAPI import WeatherAPI


class TestWeatherAPI(unittest.TestCase):
    """ Class to test the weatherAPI.py code """

    @settings(max_examples=10)
    @given(lat=st.floats(
           min_value=-90.0, max_value=90.0, allow_nan=False,
           allow_infinity=False), lon=st.floats(
           min_value=-180.0, max_value=180.0, allow_nan=False,
           allow_infinity=False))
    def test_get_weather_data(self, lat: float, lon: float) -> None:
        """ Test the get_weather_data() method """
        expected_response_json = {
            'current': {
                'temp': 72.0,
                'weather': [
                    {'description': 'clear sky', 'icon': '01d'}
                ]
            }
        }
        expected_response = MagicMock()
        expected_response.json.return_value = expected_response_json
        expected_response.status_code = 200

        with patch('requests.get', return_value=expected_response) as mock_get:
            weather_api = WeatherAPI()

            result = weather_api.get_weather_data(lat, lon)

            self.assertIsNotNone(result)
            self.assertIn('current', result)
            self.assertIn('temp', result['current'])
            self.assertIsInstance(result['current']['temp'], float)
            self.assertEqual(result['current']['temp'], 72.0)

            mock_get.assert_called_once()

    @settings(max_examples=10)
    @given(lat=st.floats(
           min_value=-90.0, max_value=90.0, allow_nan=False,
           allow_infinity=False),
           lon=st.floats(min_value=-180.0, max_value=180.0,
                         allow_nan=False, allow_infinity=False))
    def test_get_forecast_data_success(self, lat: float, lon: float) -> None:
        """ test the get_forecast_data() method success """
        expected_forecast_json = {
            'daily': [
                {'temp': {'day': 60}, 'weather': [
                    {'description': 'light rain', 'icon': '10d'}]}
            ]
        }
        expected_response = MagicMock()
        expected_response.json.return_value = expected_forecast_json
        expected_response.status_code = 200

        with patch('requests.get', return_value=expected_response) as mock_get:
            weather_api = WeatherAPI()
            forecast_data = weather_api.get_forecast_data(lat, lon)

            if forecast_data is not None:
                self.assertIsNotNone(forecast_data)
                self.assertIsInstance(forecast_data, list)
                for forecast_day in forecast_data:
                    self.assertIn('temp', forecast_day)
                    self.assertIn('weather', forecast_day)
                    self.assertEqual(len(forecast_data), len(
                        expected_forecast_json['daily']))
            else:
                self.fail("Forecast data is None")

            mock_get.assert_called_once()

    @settings(max_examples=10)
    @given(lat=st.floats(
           min_value=-90.0, max_value=90.0,
           allow_nan=False, allow_infinity=False),
           lon=st.floats(min_value=-180.0, max_value=180.0,
                         allow_nan=False, allow_infinity=False))
    def test_get_forecast_data_failure(self, lat: float, lon: float) -> None:
        """ test get_forecast_data() method failure """
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            weather_api = WeatherAPI()
            result = weather_api.get_forecast_data(lat, lon)

            self.assertIsNone(result)

            mock_get.assert_called_once()

    @given(city=st.text(min_size=1),
           state=st.text(min_size=1, max_size=2),
           country=st.text(min_size=2, max_size=2))
    @patch('requests.get')
    def test_get_coordinates_success(
             self, mock_get: MagicMock, city: str,
             state: str, country: str) -> None:
        """ test the get_coordinates() method success """
        mock_response = MagicMock()
        mock_response.json.return_value = [{"lat": 40.7128, "lon": -74.0060}]
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_coordinates(city, state, country)

        self.assertIsNotNone(result)
        self.assertEqual(result, (40.7128, -74.0060))

    @given(city=st.text(min_size=1),
           state=st.text(min_size=1, max_size=2),
           country=st.text(min_size=2, max_size=2))
    @patch('requests.get')
    def test_get_coordinates_no_match(
             self, mock_get: MagicMock, city: str,
             state: str, country: str) -> None:
        """ test the get_coordinates() method failure """
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_coordinates(city, state, country)

        self.assertIsNone(result)

    @patch('os.getenv', return_value=None)
    def test_init_without_api_key(self, mock_getenv: MagicMock) -> None:
        """ test no api key """
        with self.assertRaises(ValueError):
            WeatherAPI()


if __name__ == '__main__':
    unittest.main()
