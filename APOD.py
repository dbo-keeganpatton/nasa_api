from datetime import date
import requests
import json


TODAY = date.today()

with open('./secrets/secret.json') as f:
    secret_file = json.load(f)
    secret = secret_file.get("secret")


API_KEY = secret 
URL = 'https://api.nasa.gov/planetary/apod'
DATE = '2024-05-14'
REQUEST_URL = f"{URL}?api_key={API_KEY}&date={DATE}"


r = requests.get(REQUEST_URL)
r_json = r.json()
image_url = None


for key, value in r_json.items():
    if key == 'url':
        image_url = value

        sub_r = requests.get(image_url)
        with open(f'./images/{TODAY}.jpg', 'wb') as f:
            f.write(sub_r.content)









