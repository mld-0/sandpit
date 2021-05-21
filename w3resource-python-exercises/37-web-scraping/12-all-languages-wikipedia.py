from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

_url = 'https://www.wikipedia.org'
html = urlopen(_url)

bs = BeautifulSoup(html, 'html.parser')

languages_list = bs.find_all('a', {'class': 'link-box'})
languages_dict = dict()

for loop_language in languages_list:
    loop_link = loop_language.attrs['href']
    loop_language_str = loop_language.get_text().strip().split('\n')[0]
    loop_articles_count = ''.join(re.findall('[0-9]', loop_language.get_text().strip().split('\n')[1])) + '+'
    languages_dict[loop_language_str] = [loop_articles_count, loop_link]
    print(loop_language_str)
    print(loop_articles_count)
    print(loop_link)
    print()

#   Languages as dict, sorted by articles count
languages_dict = dict(sorted(languages_dict.items(), key=lambda x: x[1][0], reverse=True))
print("languages_dict:")
print(languages_dict)
