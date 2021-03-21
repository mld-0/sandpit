import json

#   json (string) to dict
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print(type(python_obj))
print(python_obj)

json_obj = json.loads(python_obj)
print(type(json_obj) )
print(json_obj) 


