import requests
import datetime
from requests.auth import HTTPBasicAuth
import os

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 181
AGE = 26

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": os.environ["app_id"],
    "x-app-key": os.environ["api_key"]
}


details = {
    "user": os.environ["USER"],
    "pass": os.environ['PASSWORD']
}

auth_header = {
    "Authorization": os.environ["AUTHBASIC"]
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

exercise = result["exercises"]

dt = datetime.datetime.now()

for lists in exercise:
    body = {
        "workout": {
            "name": os.environ["NAME"],
            "email": os.environ["EMAIL"],
            "date": dt.strftime("%d/%m/%Y"),
            "time": dt.strftime("%H:%M:%S"),
            "duration": lists["duration_min"],
            "exercise": lists["name"].title(),
            "calories": lists["nf_calories"],
        },
    }
    sheety_response = requests.post(url=sheety_endpoint, json=body)
    # print(sheety_response.text)


new_response = requests.get(sheety_endpoint, headers=auth_header, data=details)
# print(new_response.json())
