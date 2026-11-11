import pytest
from pydantic import ValidationError

from weather_api.models import CurrentWeather, GeoResponse, WeatherResponse


def test_current_weather_valid():
    data = {"temperature_2m": 27.0, "relative_humidity_2m": 31, "wind_speed_10m": 10.4}
    weather = CurrentWeather.model_validate(data)
    assert weather.temperature_2m == 27.0
    assert weather.relative_humidity_2m == 31


def test_humidity_above_100_fails():
    data = {"temperature_2m": 27.0, "relative_humidity_2m": 150, "wind_speed_10m": 10.4}
    with pytest.raises(ValidationError):
        CurrentWeather.model_validate(data)


def test_humidity_not_a_number_fails():
    data = {"temperature_2m": 27.0, "relative_humidity_2m": "abc", "wind_speed_10m": 10.4}
    with pytest.raises(ValidationError):
        CurrentWeather.model_validate(data)


def test_geo_response_without_results_gives_empty_list():
    response = GeoResponse.model_validate({"generationtime_ms": 0.05})
    assert response.results == []


def test_geo_response_parses_matches():
    data = {
        "results": [
            {"name": "Daman", "latitude": 20.41, "longitude": 72.83, "country": "India"}
        ]
    }
    response = GeoResponse.model_validate(data)
    assert response.results[0].name == "Daman"


def test_weather_response_nested_current():
    data = {
        "current": {"temperature_2m": 27.0, "relative_humidity_2m": 31, "wind_speed_10m": 10.4}
    }
    response = WeatherResponse.model_validate(data)
    assert response.current.wind_speed_10m == 10.4


def test_weather_response_missing_current_fails():
    with pytest.raises(ValidationError):
        WeatherResponse.model_validate({})