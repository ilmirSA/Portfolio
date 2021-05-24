import requests

api_summary = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
token = "d16b72aaa86f41d9e9c595b36e81f2676a8b56ec"
api_shorten= "https://api-ssl.bitly.com/v4/shorten"
user_input = input("Введите ссылку: ")
link=("Введите ссылку для проверки")


def shorten_link(token, user_input):
    params = {"Authorization": token}
    json_data = {"long_url": user_input}
    bitlink = requests.post(api_shorten, headers=params, json=json_data)
    try:
        bitlink.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Доступ не получен! возможно не правильно введена ссылка")
    bitlink = bitlink.json()
    try:
        return bitlink['id']
    except KeyError:
        print("id не получен!")



print("Битлинк", shorten_link(token, user_input))
bitlink=shorten_link(token, user_input)





def count_clicks(token, link):
    params = {"unit": "day",
              "units": "-1", }
    header = {"Authorization": token}
    url=api_summary.format(link)
    count = requests.get(url, headers=header, params=params)
    try:
        count.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Не правильная ссылка")
    count = count.json()
    return count["total_clicks"]




print("По  повашей ссылке прошли", count_clicks(token,bitlink),"раз(а)")
