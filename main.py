import requests
import datetime

APP_ID = APP_ID
API_KEY = API_KEY

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 181
AGE = 26

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise = input("Tell me which exercise you did: ")
parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


sheety_endpoint = "https://api.sheety.co/308a6d2782f06fc8638c04aff1163efc/myWorkouts/workouts"

exercises = result["exercises"]

dt = datetime.datetime.now()

for lists in exercises:
    body = {
        "workout": {
            "name": NAME,
            "email": EMAIL,
            "date": dt.strftime("%d/%m/%Y"),
            "time": dt.strftime("%H:%M:%S"),
            "duration": lists["duration_min"],
            "exercise": lists["name"].title(),
            "calories": lists["nf_calories"],
        },
    }
    sheety_response = requests.post(url=sheety_endpoint, json=body)
    print(sheety_response.text)
