from pkgutil import get_data

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_products = soup.find(class_='main-feed__container bot css-wevjfo').find_all(class_='adTile-title')
    data = {}
    for item in all_products:
        item_text = item.text
        item_href = "https://lalafo.kg" + item.get('href')
        print(f"{item_text}: {item_href}")

    return data


def save_to_csv(data):
    with open('data.csv') as f:
        src = f.read()


def main():
    url = "https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony/apple-iphone" \
          "/q-iphone-14-pro-max?sort_by=default&suggestion_id=38177_44330_1361"
    html = get_html(url)
    data = get_data(html)


if __name__ == '__main__':
    main()
