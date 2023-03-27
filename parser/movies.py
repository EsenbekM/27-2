import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/new/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []
    for item in items:
        duration = item.find('span', class_='info').string if item.find('span', class_='info') else ""
        info = item.find('div', class_="b-content__inline_item-link").find('div').getText().split(", ")
        film = {
            "title": item.find('div', class_="b-content__inline_item-link").find('a').string,
            "url": item.find('div', class_="b-content__inline_item-link").find('a').get("href"),
            "content": item.find('i', class_='entity').string + " " + duration,
            "year": info[0],
            "country": info[1] if len(info) == 3 else "Неизвестно",
            "genre": info[2] if len(info) == 3 else info[1],
        }
        films.append(film)
    return films


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            films.extend(current_page)
        return films
    else:
        raise Exception("Error in parser!")
