from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

_url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
html = urlopen(_url)
bs = BeautifulSoup(html, 'html.parser')

image_links = bs.find_all('img', {'src': re.compile('.jpg')})
print("image_links:")
print(type(image_links))
print([type(x) for x in image_links])
print()

for loop_link in image_links:
    print("loop_link:")
    print(type(loop_link))
    print(loop_link.name)
    print(loop_link.attrs)
    print(loop_link['src'])
    print()

