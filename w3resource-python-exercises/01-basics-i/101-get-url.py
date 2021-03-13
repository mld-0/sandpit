from http.client import HTTPConnection

url = "example.com"
conn = HTTPConnection(url)
conn.request("GET", "/")  

result = conn.getresponse()
contents = result.read() 

print(contents)
