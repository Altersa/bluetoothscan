import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

table = soup.find('table')

# 使用pandas库将表格数据读入到DataFrame对象中
df = pd.read_html(str(table))[0]

# 将数据存储到Excel文件中
df.to_excel('output.xlsx', index=False)
