import requests

api_summary = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
token = "d16b72aaa86f41d9e9c595b36e81f2676a8b56ec"
api = "https://api-ssl.bitly.com/v4/shorten"
user_input = input("Введите ссылку: ")
link=("Введите ссылку для проверки")


def shorten_link(token, user_input):
    params = {"Authorization": token}
    json_data = {"long_url": user_input}
    bitlink = requests.post(api, headers=params, json=json_data)
    bitlink.raise_for_status()
    bitlink = bitlink.json()
    return bitlink['id']


try:
    bitlink = shorten_link(token, user_input)
except requests.exceptions.HTTPError:
    print("Введите корректную ссылку!!!")

print("Битлинк", shorten_link(token, user_input))
bitlink=shorten_link(token, user_input)





def count_clicks(token, link):
    params = {"unit": "day",
              "units": "-1", }
    header = {"Authorization": token}
    url=api_summary.format(link)
    count = requests.get(url, headers=header, params=params)
    count.raise_for_status()
    count = count.json()
    return count["total_clicks"]

try:
  clicks_count = count_clicks(token, bitlink)
except requests.exceptions.HTTPError:
    print("Не удалось посчитать ")

print("По  повашей ссылке прошли", count_clicks(token,bitlink),"раз(а)")
