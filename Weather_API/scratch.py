import httpx
from weather_api.models import GeoMatch, GeoResponse,CurrentWeather, WeatherResponse

url= "https://geocoding-api.open-meteo.com/v1/search"
paramx= {
    "name" : "daman",
    "count" : 1
}

var= httpx.get(url=url, params=paramx)
print(var.json())
ac=var.json()

geo_response = GeoResponse.model_validate(ac)
# print(geo_response)

# dicrr=ac["results"][0]
of=geo_response.results[0]
# print(of)
latitude=of.latitude
longitude=of.longitude
print(latitude,longitude)

url2="https://api.open-meteo.com/v1/forecast"
paramy={
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

var2=httpx.get(url=url2,params=paramy)
az=var2.json()
print(az)

current=WeatherResponse.model_validate(az)

print(current)
