from pyquery import PyQuery as pq
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
html = requests.get('https://www.zhihu.com/explore#daily-hot', headers=headers).text
doc = pq(html)
items = doc('.explore-feed.feed-item').items()
for item in items:
    question = item.find('.question_link').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    with open('1.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 300 + '\n')
