from pyquery import PyQuery as pq
import requests
html = requests.get('http://www.163.com').text
# print(html)
doc = pq(html)
print(doc('img'))