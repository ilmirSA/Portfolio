import requests
link_shorten= "https://api-ssl.bitly.com/v4/shorten"
token = "d16b72aaa86f41d9e9c595b36e81f2676a8b56ec"
user_input = input("Введите ссыллку : ")


def shorten_link(token, user_input):
    params = {"Authorization": token}
    json_data = {"long_url": user_input}
    response = requests.post(link_shorten, headers=params, json=json_data)
    response.raise_for_status()
    bitlink = response.json()
    return bitlink['id']

try:
    bitlink= shorten_link(token, user_input)
except requests.exceptions.HTTPError:
    print("Введите корректную ссылку!!!")

link=shorten_link(token, user_input)

def count_clicks(token,link)
    a="https://api-ssl.bitly.com/v4/bitlinks/bit.ly/2KVuKDJ/clicks/summary"
    b=a.format(link)
    print(b)



