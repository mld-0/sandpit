from urllib.request import urlopen
from bs4 import BeautifulSoup

_url = 'https://en.wikipedia.org/wiki/Python'
html = urlopen(_url)

#bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html, features='lxml')
print("bs:")
print(type(bs))
print()

for loop_link in bs.find_all("a"):
    loop_url = None
    loop_text = None
    #   Get tag text, or alternatively alt text of first child (if it can be found)
    if len(loop_link.text) > 0:
        loop_text = loop_link.text
    if len(loop_link.contents) > 0:
        if hasattr(loop_link.contents[0], 'alt'):
            if 'alt' in loop_link.contents[0].attrs.keys():
                loop_text = loop_link.contents[0].attrs['alt']
    #   Get link if it can be found
    if 'href' in loop_link.attrs:
        loop_url = loop_link.attrs['href']
    print(loop_text)
    print(loop_url)
    print()


