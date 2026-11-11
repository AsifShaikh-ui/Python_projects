from pydantic import BaseModel , Field
from typing import List, Annotated

class GeoMatch(BaseModel):
    name: str
    latitude: float
    longitude: float
    country: str

class GeoResponse(BaseModel):
    results: Annotated[list[GeoMatch],Field(default=[])]

class CurrentWeather(BaseModel):
    temperature_2m: float
    relative_humidity_2m: Annotated[int,Field(ge=0 ,le=100)]
    wind_speed_10m: float

class WeatherResponse(BaseModel):
    current : CurrentWeather

class CityWeather(BaseModel):
    city: GeoMatch
    weather: CurrentWeather
