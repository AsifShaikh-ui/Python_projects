import httpx

GEOCODING_URL= "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL="https://api.open-meteo.com/v1/forecast"
GET_URL = "https://httpbin.org/get"
POST_URL = "https://httpbin.org/post"
PUT_URL = "https://httpbin.org/put"
PATCH_URL = "https://httpbin.org/patch"
DELETE_URL = "https://httpbin.org/delete"
data = {
    "name" : "Daman",
    "count" : 1
}

# response = httpx.get(url=GEOCODING_URL, params=data)
# print(response.url)
# print(response.status_code)
# print(response.headers['content-type'])
# print(response.elapsed)

response = httpx.get(url=GET_URL, params=data)
print(response.status_code)
print(response.json())
print("------------------------------")

response_1 = httpx.post(url=POST_URL, json=data)
print(response_1.status_code)
print(response_1.json())
print("------------------------------")

response_2 = httpx.put(url=PUT_URL, data=data)
print(response_2.status_code)
print(response_2.json())
print("------------------------------")

response_3 = httpx.patch(url=PATCH_URL, json=data)
print(response_3.status_code)
print(response_3.json())
print("------------------------------")

response_4 = httpx.delete(url=DELETE_URL, params=data)
print(response_4.status_code)
print(response_4.json())
