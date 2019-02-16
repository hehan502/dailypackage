
from pyquery import PyQuery as pq
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
html = requests.get('http://www.tu11.com/xingganmeinvxiezhen/', headers=headers)
html.encoding = 'gb2312'
r =html.text
doc = pq(r)
# print(r)

items = doc('.img-responsive.picheng').items()
for item in items:
    get_img = item.attr('src')
    file_name = item.attr('alt')
    img = requests.get(get_img,headers=headers)

    # print (img,file_name)
    with open(file_name +'.jpg','wb') as f:
        f.write(img.content)
        print (file_name)
