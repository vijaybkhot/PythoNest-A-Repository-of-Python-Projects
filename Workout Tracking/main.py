import json
from datetime import datetime
import requests
import os

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 1833
AGE = 33

APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_API_KEY")

# Nutritionix API endpoint and headers
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers_nutritionix = {
    "Content-Type": 'application/json; charset=utf-8',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

# User input for exercises
exercise_text = input("Tell me which exercises you did: ")

# Data for the Nutritionix API request
data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Making a POST request to Nutritionix API
response_workout = requests.post(url=exercise_endpoint, headers=headers_nutritionix,
                                 data=json.dumps(data, ensure_ascii=False))
workout_json = response_workout.json()
print(f"Nutritionix API call: \n {workout_json} \n")

# Getting current date and time
today = datetime.now()
date_today = datetime.strftime(today, '%d/%m/%Y')
now_time = today.strftime("%X")

# Google Sheet details
GOOGLE_SHEET_NAME = "workout"
sheety_input = {}
for exercise in workout_json['exercises']:
    # Building input data for Sheety API
    sheety_input = {
        GOOGLE_SHEET_NAME: {
            "date": date_today,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

# Sheety API endpoint and headers
sheety_post_endpoint = os.environ.get("SHEETY_POST_ENDPOINT")
bearer = os.environ.get("BEARER")
headers_sheety_bearer = {
    "Authorization": f"Bearer {bearer}",
    "Content-Type": 'application/json',
}

# Making a POST request to Sheety API
response_sheety = requests.post(url=sheety_post_endpoint, json=sheety_input, headers=headers_sheety_bearer)
sheety_text = response_sheety.text
print(sheety_text)



