import requests
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

API_KEY = "d83e26fc5b59e67f9e60382bf1bbedc4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
location = geolocator.geocode(city)

latitude = location.latitude
longitude = location.longitude

request_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'].title()
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} celsius")
else:
    print("Some error occured")




