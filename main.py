import requests

APP_ID = "b2a5beb0"
API_KEY = "72636b18cb95a98b24a9ab53a64dad13"

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
