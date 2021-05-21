import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

_url = 'https://en.wikipedia.org/wiki/Main_Page'

r = requests.get(_url)
bs = BeautifulSoup(r.text, 'html.parser')
#   or
r = urlopen(_url)
bs = BeautifulSoup(r, 'html.parser')

print("bs:")
print(type(bs))
print()

_tags = ['h' + str(i) for i in range(1, 7)]
print("_tags:")
print(_tags)
print()

titles = bs.find_all(_tags)

print("titles:")
print(type(titles))
print([type(x) for x in titles])
print()

for loop_title in titles:
    print(loop_title)
    print(loop_title.text.strip())
    print()


