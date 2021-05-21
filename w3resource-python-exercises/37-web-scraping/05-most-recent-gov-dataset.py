from lxml import html
import requests

_url = 'http://catalog.data.gov/dataset?q=&sort=metadata_created+desc'
r = requests.get(_url)

#_doc = html.fromstring(r.text)
_doc = html.fromstring(r.content)
print("_doc:")
print(type(_doc))
print(_doc)
print()

_css_headings = _doc.cssselect('h3.dataset-heading')
print('_css_headings:')
print(_css_headings)
print()

_css_heading_text = [x.text_content().strip() for x in _css_headings]
print("_css_heading_text:")
print(_css_heading_text)
print()

_top_heading_str = _css_headings[0].text_content()
_top_heading_str = _top_heading_str.strip()
print("_top_heading_str:")
print(_top_heading_str)

