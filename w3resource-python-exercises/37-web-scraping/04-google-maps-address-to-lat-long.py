import requests

_url = 'http://maps.googleapis.com/maps/api/geocode/json'

_address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India', 'language': 'en'}

r = requests.get(_url, params=_address)

#   Request denied: Google require an API key be used to interact with their services
result = r.json()
print("result:")
print(result)


