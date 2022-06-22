import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 13.082680
MY_LNG = 80.270721
EMAIL = "jostheboss@ecb.com"
PASSWORD = "498/4"

# Check if ISS is near my location
def is_iss_overhead():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()

    data = res.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

# Check if it's night
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()

    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="england@ecb.com",msg="Subject:Look Up\n\nThe ISS is above your location")
