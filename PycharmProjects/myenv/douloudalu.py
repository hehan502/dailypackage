import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


i = 15379610
while i <= 15380350:
    url = 'http://www.quanshuwang.com/book/44/44683/{}.html'.format(i)
    html = requests.get(url,headers=headers)
    html.encoding = 'gbk'
    doc = pq(html.text)
    items = doc('#container .bookInfo').items()
    for item in items:
            title = doc('h1').text()
            content = doc('.mainContenr').text()
            with open('22.txt','a',encoding='utf-8') as f:
                f.write('\n'.join([title,content]))
                f.write('\n' + '='*100 + '\n')
    i = i + 1
    print('正在打印第%r页'%i)


