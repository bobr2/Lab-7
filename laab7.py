import requests
import json
import requests
from PIL import Image
from io import BytesIO


city_name = 'London'
key1 = '2f44ab8d94825710392977b37c24d3ac'
response_l = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key1}')
result = json.loads(response_l.text)
print(result)

headers = {
    'X-API-KEY': "6B6QVDX-PNB4SYP-K2254WW-VCG66QW"
}

url = 'https://api.kinopoisk.dev/v1.4/movie?rating.kp=8-10&year=2023'
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    movie_info = response.json()
    
    for x in movie_info["docs"]:
        otvet = {
            "name" : x["name"],
            "nameEn" : x["alternativeName"],
            "rating" : (x["rating"])["kp"],
            "year" : x["year"],
            "type" : x["type"],
            "votes" : (x["votes"])["kp"],
            "описание" : x["description"]
        }
        print(otvet)
        print("---------------")
else:
    print(f"Error {response.status_code}: {response.text}")


key = "h0Ue0DHN1cqUoIIyjgSm9GxLYKgOS1LkwsJHw3sc"
url = f'https://api.nasa.gov/planetary/apod?api_key={key}'
response = requests.get(url=url)
res = response.json()


def display_image_from_url(url):
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
        
    img.show()



urlq = res["url"]
display_image_from_url(urlq)