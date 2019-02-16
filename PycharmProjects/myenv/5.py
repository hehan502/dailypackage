import requests
from pyquery import PyQuery as pq
import random
import time


headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'https://www.meitulu.com/item/16290_10.html'
html = requests.get(url,headers=headers).text
doc = pq(html)
links = doc('.content img')

for link in links:
    image_url = pq(link).attr('src')
    image_alt = random.randrange(0,1000,4)
    response = requests.get(image_url, headers=headers)
    path_name = 'downloadimg/{}.jpg'.format(image_alt)
    print(image_url)

    with open(path_name, 'wb') as f:
        f.write(response.content)
        f.close()
        time.sleep(1)


















