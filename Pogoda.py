import requests

pattern = 'http://wttr.in/{}'

dict = {
    "Лондон?nTqmM&lang=ru": "",
    "Шереметьево?nTqm&lang=ru": "",
    "Череповец?nTqm&lang=ru": "",
}

for city in dict:
    url = pattern.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
