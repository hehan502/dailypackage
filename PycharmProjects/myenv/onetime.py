import requests
from pyquery import PyQuery as pq

html = requests.get('http://www.hbzhan.com/st537293/Article_495568.html')
html.encoding = 'utf-8'
doc = pq(html.text)

d = doc('.innewscontent').text()
print(d)
