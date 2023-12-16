import requests
from bs4 import BeautifulSoup

url='https://stackoverflow.com/questions/tagged/python'
reqs = requests.get(url)
if reqs.status_code==200:
    soup = BeautifulSoup(reqs.text, 'html.parser')
    links=soup.find_all('a')
    for link in links:
        if link.has_attr('title'):
            print(link.title)
        else:
            print(link.text.strip())
else:
    print('Failed')