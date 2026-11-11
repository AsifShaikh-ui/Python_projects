import asyncio
from weather_api.client_async import CityNotFoundError, get_city_weather
import time



# def main() -> None:
    
#     text = input("Enter city names separated by commas: ")
#     cities = [name.strip() for name in text.split(",")]
#     start = time.time()
#     for city_name in cities:
#         try:
#             result = asyncio.run(get_city_weather(city_name))
#         except CityNotFoundError:
#             print("City not found:", city_name)
#             print()
#             continue

#         print(result.city.name, result.city.country)
#         print(f"Temperature: {result.weather.temperature_2m}°c")
#         print(f"Humidity: {result.weather.relative_humidity_2m}%")
#         print(f"Wind: {result.weather.wind_speed_10m}km/h")
#         print()

#     end = time.time()
#     print(end - start)

async def fetch_all(cities: list[str]):

    jobs = [get_city_weather(city) for city in cities]
    results = await asyncio.gather(*jobs, return_exceptions=True)
    return results

def main() -> None:
    
    text = input("Enter city names separated by commas: ")
    cities = [name.strip() for name in text.split(",")]

    start = time.time()
    results = asyncio.run(fetch_all(cities))
    
    for city_name, result in zip(cities, results):
        if isinstance(result, CityNotFoundError):
            print("City not found:", city_name)
            print()
            continue
        
        if isinstance(result, Exception):
            print(f"Something Get Wrong For {city_name} - {result}")
            print()
            continue
            

        print(result.city.name, result.city.country)
        print(f"Temperature: {result.weather.temperature_2m}°c")
        print(f"Humidity: {result.weather.relative_humidity_2m}%")
        print(f"Wind: {result.weather.wind_speed_10m}km/h")
        print()
    end = time.time()
    print(end - start)
    
if __name__ == "__main__":
    main()