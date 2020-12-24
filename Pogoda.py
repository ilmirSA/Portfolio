import requests

cities = ["London", "Sheremetyevo", "Cherepovets"]
pattern = 'http://wttr.in/{}?n'
for insert in cities:
    url = pattern.format(insert)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
