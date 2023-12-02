# beautifulsoupでWEBスクレピング
# WEBページの中身のタグを見て、どういったものがあるのか
# 解析したり調べていくこと

from bs4 import BeautifulStoneSoup
import requests


html = requests.get('http://www.python.org')

soup = BeautifulSoup(html.text, 'lxml')

titles = soup.find_all('title')
print(titles[0].text)


intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)


