#! /usr/bin/env python3
"""
This module handles web requets and routes
This module gets weather data into expected formmat
"""
from flask import Flask, request, render_template
from datetime import datetime, timezone
from weatherAPI import WeatherAPI
from typing import Tuple, Union


class WeatherApp:
    """ This class contains the logic for the web app itself """
    def __init__(self) -> None:
        """ Initialize required methods """
        self.app = Flask(__name__)
        self.weather_api = WeatherAPI()
        self.setup_routes()
        self.register_filters()

    def register_filters(self) -> None:
        """ Contain the custom date logic """
        @self.app.template_filter()
        def date(unix_timestamp: float, format: str = "%Y-%m-%d") -> str:
            """ Convert a UNIX timestamp to a formatted string """
            utc_time = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
            return utc_time.strftime(format)
        self.app.jinja_env.filters['date'] = date

    def setup_routes(self) -> None:
        """ Setup the routes for the web server """
        @self.app.route('/', methods=['GET', 'POST'])
        # def home() -> str:
        def home() -> Union[str, Tuple[str, int]]:
            """ Handle request from web server """
            if request.method == 'POST':
                city = request.form['city']
                state = request.form.get('state', '')
                coordinates = self.weather_api.get_coordinates(
                    city, state=state)
                # print(f"Coordinates for {city}, {state}: {lat}, {lon}")
                if coordinates is None:
                    return "Location not found", 404
                lat, lon = coordinates
                if lat is None or lon is None:
                    return "Location not found", 404
                if lat is not None and lon is not None:
                    current_weather = self.weather_api.get_weather_data(
                        lat, lon)
                    daily_forecast = self.weather_api.get_forecast_data(
                        lat, lon)
                    # print(f"Weather Data: {current_weather}")

                    if current_weather and daily_forecast:
                        temp_f = current_weather['current']['temp']
                        description = current_weather[
                            'current']['weather'][0]['description']
                        icon_code = current_weather[
                            'current']['weather'][0]['icon']
                        return render_template(
                            'weather.html', daily_forecast=daily_forecast,
                            temp_f=temp_f, description=description,
                            city=city, icon_code=icon_code)
                    else:
                        print("Current weather data not found in response")
                        return "Weather data not found", 404
                else:
                    return "Location not found", 404
            return render_template('form.html')

    def run(self) -> None:
        """ Run the weather app """
        self.app.run(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    app = WeatherApp()
    app.run()
