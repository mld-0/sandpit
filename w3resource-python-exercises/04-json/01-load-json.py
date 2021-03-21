import json

json_str =  '{ "Name": "David", "Class": "I", "Age": 6 }'

json_dict = json.loads(json_str)
print(type(json_dict))
print(json_dict)

for k, v in json_dict.items():
    print(k, v)

