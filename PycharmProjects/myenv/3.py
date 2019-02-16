import requests
from pyquery import PyQuery as pq
import random


headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

for i in range(2,12):
    url = 'https://www.meitulu.com/item/16290_{}.html'.format(i)
    html = requests.get(url,headers=headers).text
    doc = pq(html)
    links = doc('.content img')

    for link in links:
        image_url = pq(link).attr('src')
        image_alt = random.randrange(0,1000,4)
        response = requests.get(image_url, headers=headers)
        path_name = 'downloadimg/{}.jpg'.format(image_alt)
        print(path_name,image_url)

        # with open(path_name, 'wb') as f:
        #     f.write(response.content)
        #     f.close()














def save_image(content):
    for i in range(1000):
        path_name = 'downloadimg/{}.jpg'.format(i)
        with open(path_name,'wb') as f:
            print(path_name )
            f.write(content)
            f.close()

def main(page):
    print('===============开始抓取第%r页==============='%page)
    url = 'https://www.meitulu.com/item/16290_{}.html'.format(page)
    html = get_page(url)
    if html:
        urls=parse_page(html)
        for url in urls:
            print('正在下载:%r'%url)
            content=download_image(url)
            save_image(content)



