import smtplib as smtp
import requests
from datetime import datetime

MY_LAT = 13.067439  # Your latitude
MY_LONG = 80.237617  # Your longitude
MY_EMAIL = "prasannaragav29@gmail.com"
PASSKEY = "uypazguixpssrxls"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
def checkLoc():
    if  iss_latitude > MY_LAT-6 and iss_latitude <= MY_LAT+6 and iss_longitude > MY_LONG-6 and iss_longitude > MY_LONG+6:
        print("ISS Location is close-by.")
        return True
    else:
        print("ISS Location is not close-by.")
        return False


def generate_mail():
    with smtp.SMTP(host="smtp.gmail.com",port=587) as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=PASSKEY)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: International Space Station Visible Alert\n\n ISS is visible above your skies check it out"
        )
        print("ISS near location and sky is dark. Mail triggered!")


def checkVisbl():
    if time_now.hour < sunrise and time_now.hour>=sunset:
        print("The Sky should be dark.")
        return True
    else:
        print("The Sky is not dark.")
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
loc = checkLoc()
visible = checkVisbl()
if loc and visible:
    generate_mail()

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



