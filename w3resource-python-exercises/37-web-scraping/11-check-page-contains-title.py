import requests
from bs4 import BeautifulSoup

def check_page_title(url):
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        return None

    try:
        bs = BeautifulSoup(r.content, 'lxml')
        #   Ongoing: 2021-05-17T20:05:53AEST (searching for and) accessing attributes, differences between (see below):
        title = bs.body.h1
        title = bs.find('body').find('h1')
    except Exception as e:
        print(e)
        return None

    print(title)

_urls = ['https://www.w3resource.com/', 'https://www.example.com/'] 

for loop_url in _urls:
    print("loop_url=(%s)" % loop_url)
    check_page_title(loop_url)
    print()

