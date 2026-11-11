import asyncio

import httpx
import pytest

from weather_api.client_async import (
    CityNotFoundError,
    find_city,
    get_city_weather,
    get_weather,
)

GEO_DATA = {
    "results": [
        {"name": "Daman", "latitude": 20.41, "longitude": 72.83, "country": "India"}
    ]
}
WEATHER_DATA = {
    "current": {"temperature_2m": 27.0, "relative_humidity_2m": 31, "wind_speed_10m": 10.4}
}


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data


def patch_get(monkeypatch, handler):
    async def fake_get(self, url, **kwargs):
        return handler(url)

    monkeypatch.setattr(httpx.AsyncClient, "get", fake_get)


def test_find_city_returns_match(monkeypatch):
    patch_get(monkeypatch, lambda url: FakeResponse(GEO_DATA))
    city = asyncio.run(find_city("daman"))
    assert city.name == "Daman"
    assert city.country == "India"


def test_find_city_not_found_raises(monkeypatch):
    patch_get(monkeypatch, lambda url: FakeResponse({"generationtime_ms": 0.05}))
    with pytest.raises(CityNotFoundError):
        asyncio.run(find_city("asdfgh"))


def test_get_weather_returns_current(monkeypatch):
    patch_get(monkeypatch, lambda url: FakeResponse(WEATHER_DATA))
    weather = asyncio.run(get_weather(20.41, 72.83))
    assert weather.temperature_2m == 27.0


def test_get_city_weather_combines_both(monkeypatch):
    def handler(url):
        if "geocoding" in url:
            return FakeResponse(GEO_DATA)
        return FakeResponse(WEATHER_DATA)

    patch_get(monkeypatch, handler)
    result = asyncio.run(get_city_weather("daman"))
    assert result.city.name == "Daman"
    assert result.weather.relative_humidity_2m == 31


def test_network_failure_is_raised(monkeypatch):
    def handler(url):
        raise httpx.ConnectError("no internet")

    patch_get(monkeypatch, handler)
    with pytest.raises(httpx.ConnectError):
        asyncio.run(find_city("daman"))