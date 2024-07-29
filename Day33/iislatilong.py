import requests
import datetime


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# lat = data["iss_position"]["latitude"]
# lon = data["iss_position"]["longitude"]
# iss_curr_location = (lat, lon)
# print(iss_curr_location)

parameters = {
    "lat": 13.067439,
    "lng": 80.237617,
    "tzid": "Asia/Kolkata",
    "formatted": 0

}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sun_rise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sun_set = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sun_rise,sun_set)
print(data)

