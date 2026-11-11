import httpx
from weather_api.models import CityWeather, GeoResponse, WeatherResponse

url= "https://geocoding-api.open-meteo.com/v1/search"
url2="https://api.open-meteo.com/v1/forecast"

class CityNotFoundError(Exception):
    """Raised when the geocoding API finds no match for a city name."""

def find_city(city: str):


    paramx= {
        "name" : city,
        "count" : 1
    }

    fetch_geo_location= httpx.get(url=url, params=paramx)
    response = fetch_geo_location.json()

    city_found = GeoResponse.model_validate(response)
    if  not city_found.results:
        raise CityNotFoundError(f"No city found for '{city}'")
   
    city_coordinates = city_found.results[0]

    return city_coordinates

def get_weather(latitude:float, longitude:float):

    paramy={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    fetch_detail=httpx.get(url=url2,params=paramy)
    detail_response=fetch_detail.json()

    current=WeatherResponse.model_validate(detail_response)

    return current.current


def get_city_weather(city_name: str) -> CityWeather:
    city = find_city(city_name)
    weather = get_weather(city.latitude, city.longitude)

    return CityWeather(city=city, weather=weather)
