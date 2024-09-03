import requests
from bs4 import BeautifulSoup

url = "https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

titles = soup.find_all('body')

with open('titles.txt', 'w' , encoding='utf-8') as f:
    for title in titles:
        f.write(title.test + '\n')
