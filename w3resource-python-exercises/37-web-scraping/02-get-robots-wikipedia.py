import requests

_url = 'https://en.wikipedia.org/robots.txt'
print("_url:")
print(_url)
print()

r = requests.get(_url)
print("r:")
print(type(r))
print(r)

_robots_text = r.text
print("_robots_text")
print(type(_robots_text))
print(_robots_text)

