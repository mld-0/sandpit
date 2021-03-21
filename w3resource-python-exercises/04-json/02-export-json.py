import json

json_dict = {
  "name": "David",
  "class": "I",
  "age": 6  
}

json_str = json.dumps(json_dict)
print(type(json_str))
print(json_str)
