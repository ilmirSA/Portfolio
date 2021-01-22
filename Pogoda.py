import requests

url = 'http://wttr.in/{}'

cities = ["Лондон", "Шереметьево", "Казань", ]

value = {"nTqmM": "",
         "lang": "ru", }

for city in cities:
    response = url.format(city)
    response = requests.get(response, params=value)
    response.raise_for_status()
    print(response.text)
