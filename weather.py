import requests

geo_url = "https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=10&language=en&format=json"

weather_url = "https://api.open-meteo.com/v1/forecast"

city = input("Enter City Name : ")

geo_param = {
    "name" : city,
    "count" : 1,
}
response1 = requests.get(geo_url , params=geo_param , timeout=10).json()
data = response1["results"][0]
nam = data["name"]
lat = data["latitude"]
lon = data["longitude"]

wea_para = {
    "name":nam,
    "latitude":lat,
    "longitude":lon,
    "current":["temperature_2m",
               "relative_humidity_2m",
               "apparent_temperature",
               "wind_speed_10m",
               ],
               "timezone":"Asia/Kolkata"
}
response = requests.get(weather_url , params=wea_para , timeout=10).json()
result = response["current"]
temp = result["temperature_2m"]
humi = result["relative_humidity_2m"]
apptemp = result["apparent_temperature"]
wind = result["wind_speed_10m"]
Time = result["time"]
print("___Weather Info___")
print("City :",nam)
print("Time : ",Time)
print("Latitude :",lat)
print("Longitude :",lon)
print("Temperature :" , temp,"°C")
print("Humidity :" , humi,"%")
print("Apparent Temperature :",apptemp,"°C")
print("Wind Speed :",wind,"Km/h")


