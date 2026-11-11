# Weather CLI

A command-line tool that shows the current weather for several cities at once. It fetches all cities **concurrently** with `asyncio`, and validates every API response with **Pydantic**.

Data comes from the free [Open-Meteo](https://open-meteo.com/) APIs, which need no API key.

## Features

- Current temperature, humidity and wind speed for any number of cities
- Cities are fetched at the same time, not one after another
- Shows the matched city and country, so a wrong guess by the geocoder is visible
- A bad city name doesn't stop the other cities
- Typed code, validated data models and automated tests

## Project structure

```
Weather_API/
├── pyproject.toml
├── uv.lock
├── src/weather_api/
│   ├── models.py        # Pydantic models (no network code)
│   ├── client_async.py  # async API calls, returns validated models
│   ├── client.py   # original sync version, kept for benchmarking
│   └── cli.py           # reads input and prints results
└── tests/
    ├── test_models.py
    └── test_client.py
```

## Setup

Requires Python 3.13 and [uv](https://docs.astral.sh/uv/).

```
uv sync
```

## Usage

```
uv run src\weather_api\cli.py
```

When asked, type city names separated by commas:

```
Enter city names separated by commas: Surat, Mumbai, Delhi
```

Example output:

```
Surat India
Temperature: 27.0 °C
Humidity: 31 %
Wind: 10.4 km/h
```

A city that can't be found prints `City not found: <name>`, and the others still show.

## Tests

```
uv run pytest -v
```

Model tests use plain dictionaries. Client tests replace the HTTP call with a fake, so no real network access is needed.

## How it works

1. `find_city` calls the geocoding API and returns the first match, or raises `CityNotFoundError` if there is none.
2. `get_weather` calls the forecast API with that city's coordinates.
3. `get_city_weather` combines both into one `CityWeather` object.
4. `cli.py` runs one `get_city_weather` job per city with `asyncio.gather(..., return_exceptions=True)`.

## Benchmark

Same 5 cities, fetching only (no printing), median of 3 runs:

| Version | Time |
|---|---|
| Sequential (`client_sync.py`) | 12.33 s |
| Concurrent (`client_async.py`) | 3.97 s |

About **3.1 X faster**. Concurrent time is close to the slowest single request, because the network waits overlap.

## Built with

Python, uv, httpx, Pydantic, asyncio, pytest