import requests

url = 'http://wttr.in/{}'

key = ["Лондон", "Шереметьево", "Череповец", ]

value = {"nTqmM": "",
         "lang": "ru", }

for city in key:
    response = url.format(city)
    response = requests.get(response, params=value)
    response.raise_for_status()
    print(response.text)
