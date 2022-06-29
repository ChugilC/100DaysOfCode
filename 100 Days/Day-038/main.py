import requests
from datetime import datetime

APP_ID = "YOUR_ID"
API_KEY = "YOUR_KEY"
TYPE = "application/json"

GENDER = "male"
HEIGHT = 00
WEIGHT = 00
AGE = 00

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": TYPE
}

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("What did you do today: ")

nutritionix_body = {
    "query": user_input,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT

}

sheety_url = "https://api.sheety.co/RANDOM_KEY/myWorkouts/workouts"

response = requests.post(url=nutritionix_url, headers=nutritionix_headers, json=nutritionix_body)

result = response.json()["exercises"][0]

response_duration = result["duration_min"]
response_exercise = result["name"].title()
response_calories = result["nf_calories"]
today = datetime.now()
response_date = today.strftime("%d/%m/%Y")
response_time = str(today).split(" ")[1].split(".")[0]

sheety_body = {
    "workout": {
        "date": response_date,
        "time": response_time,
        "exercise": response_exercise,
        "duration": response_duration,
        "calories": response_calories
    }
}

sheety_headers = {
    "Content-Type": TYPE
}

sheety_response = requests.post(url=sheety_url, headers=sheety_headers, json=sheety_body, auth=("USERNAME", "PASSWORD"))