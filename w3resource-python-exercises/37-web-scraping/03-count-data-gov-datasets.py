import requests
from lxml import html

_url = 'https://www.data.gov'
print('_url:')
print(_url)
print()

r = requests.get(_url)
print('r:')
print(type(r))
print(r)
print()

_doc = html.fromstring(r.text)
print('_doc:')
print(type(_doc))
print(_doc)
print()

#   The number is contained in the only hyperlink on the page contained in a small tag -> use this fact to extract it
_link = _doc.cssselect('small a')[0]
print('_link:')
print(type(_link))
print(_link)
print()

_text = _link.text
print('_link:')
print(type(_text))
print(_text)


