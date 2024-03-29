#! /usr/bin/env python3
"""
This module interfaces with WeatherMap API to get weather data
Helpful: https://openweathermap.org/api/one-call-3#current
https://openweathermap.org/api/geocoding-api
"""

import os
import requests  # add requests to requirements.txt
from typing import Tuple, Optional, Dict, List, Any, Union


class WeatherAPI:
    """ This class contains logic for interacting with the API """
    def __init__(self) -> None:
        """ Initialize the API key and url for API calls"""
        self._api_key: str = os.getenv("WEATHER_API_KEY") or ""
        if not self._api_key:
            raise ValueError("API key not provided")
        self._base_url: str = "https://api.openweathermap.org/data/3.0/onecall"

    @property
    def api_key(self) -> str:
        """ Getter for api_key """
        return self._api_key

    @property
    def base_url(self) -> str:
        """ Getter for base_url """
        return self._base_url

    def get_weather_data(self, lat: float, lon: float) -> Dict[str, Any]:
        """ Method to get weather data for a city """
        params: Dict[str, Any] = {
            'lat': lat,
            'lon': lon,
            'exclude': 'minutely, hourly',
            'units': 'imperial',
            'appid': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        json_content: Union[Dict[str, Any], None] = response.json()
        if json_content is None:
            raise ValueError("Recieved empty JSON content")
        return json_content

    def get_forecast_data(
            self, lat: float, lon: float) -> Optional[List[Dict[str, Any]]]:
        """ Method to get daily forecast data """
        params: Dict[str, Any] = {
            'lat': lat,
            'lon': lon,
            'exclude': 'current, minutely, hourly, alerts',
            'units': 'imperial',
            'appid': self.api_key
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            forecast_data: Optional[Dict[str, Any]] = response.json()
            if forecast_data and 'daily' in forecast_data:
                return forecast_data.get('daily')
            else:
                raise ValueError("Recieved empty forecast data")
        else:
            print(
                f"Error fetching daily forecast data: {response.status_code}")
            return None

    def get_coordinates(
            self, city: str, state: Optional[
                str] = None, country: str = 'US') -> Optional[
                    Tuple[float, float]]:
        """ Method to get coordinates for given city, state, country """
        query = f"{city}, {state}, {country}".strip(',')
        params: Dict[str, Any] = {
            'q': query,
            'limit': 1,
            'appid': self.api_key
        }

        geocode_url = "https://api.openweathermap.org/geo/1.0/direct"
        response = requests.get(geocode_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            return None
