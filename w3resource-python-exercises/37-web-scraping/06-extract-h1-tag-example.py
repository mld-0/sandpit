from urllib.request import urlopen
from bs4 import BeautifulSoup

_url = 'https://www.example.com/'
r = urlopen(_url)
print("r:")
print(type(r))
print(r)
print()

bsh = BeautifulSoup(r.read(), 'html.parser')
print("bsh:")
print(type(bsh))
print(bsh)
print()

print("bsh.h1:")
print(type(bsh.h1))
print(bsh.h1)

