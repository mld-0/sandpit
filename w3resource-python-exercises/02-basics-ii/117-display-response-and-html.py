import requests

url = 'http://www.example.com'
print("URL: ", url)

r = requests.get(url)
print("Web page status: ", r)

if r.ok:
    print("HTML:")
    print(r.text)

