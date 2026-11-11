import httpx
from weather_api.models import CityWeather, GeoResponse, WeatherResponse

GEOCODING_URL= "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL="https://api.open-meteo.com/v1/forecast"

class CityNotFoundError(Exception):
    """Raised when the geocoding API finds no match for a city name."""

async def find_city(city: str):


    param= {
        "name" : city,
        "count" : 1
    }

    async with httpx.AsyncClient() as client:
        fetch_geo_location= await client.get(url=GEOCODING_URL, params=param)

    response = GeoResponse.model_validate(fetch_geo_location.json())

    if  not response.results:
        raise CityNotFoundError(f"No city found for '{city}'")
   
    city_coordinates = response.results[0]

    return city_coordinates

async def get_weather(latitude:float, longitude:float):

    param={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    async with httpx.AsyncClient() as client:
        fetch_detail=await client.get(url=FORECAST_URL,params=param)

    response=WeatherResponse.model_validate(fetch_detail.json())


    return response.current


async def get_city_weather(city_name: str) -> CityWeather:
    city = await find_city(city_name)
    weather = await get_weather(city.latitude, city.longitude)

    return CityWeather(city=city, weather=weather)
