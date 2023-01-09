import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://www.nix.ru/"
r = requests.get(URL_TEMPLATE)
print()
print('Ответ от сервера:')
print(r.status_code)
#print(r.text)

soup = bs(r.text, "html.parser")
news_names = soup.find_all('div', class_='lmenu_item')
print()
print('Список ссылок:')
for name in news_names:
   print(name.a['href'])
print()
print('Пункты меню:')
print(news_names)

news_names_inf = soup.find_all('a', class_='np')
