import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)

xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, 'xml')
news_list = soup_page.findAll('item')

for loop_news in news_list:
    print(loop_news.title.text)
    print(loop_news.pubDate.text)
    print()
