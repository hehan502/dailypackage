from aip import AipOcr

APP_ID = '10716960'
API_KEY = 'GyWa1B34alrmT8dEb0pGFN6S'
SECRET_KEY = '2rIaiS9nLQoTKPzfT54GM1Ach5g3hxCA'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

image = get_file_content('img/3.jpg')
doc = client.basicGeneral(image)
print(doc)
docss = doc['words_result']
for docs in docss:
    with open('mybaiduocr.txt','a',encoding='utf-8') as f:
        f.write(docs['words'])






















