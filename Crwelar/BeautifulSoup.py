#coding:utf-8
from bs4 import BeautifulSoup
import requests
html = 'https://www.toutiao.com/a6375738133513765122/'
contents = requests.get(html).content
soup = BeautifulSoup(contents,'lxml')
description = soup.find(attrs={"name":"description"})['content']
print  description
# titles = soup.find_all('meta name="description"')
# for title in titles:
#     print title.text


