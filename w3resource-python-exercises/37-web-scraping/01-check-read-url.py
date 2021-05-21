from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def check_read_page(url_str):
    _response = None
    try:
        _response = urlopen(url_str)
    except HTTPError as e:
        print("HTTPError e=(%s)" % str(e))
    except URLError as e:
        print("URLError e=(%s)" % str(e))
    else:
        print("_response:")
        print(type(_response))
        print(_response)
        _page = _response.read()
        print("page:")
        print(type(_page))
        print(_page)

check_urls = ['https://abcxyz.com', 'https://www.example.com/']

for loop_url in check_urls:
    print("loop_url=(%s)" % loop_url)
    check_read_page(loop_url)
    print()
