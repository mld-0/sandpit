import json

j_str = {'4': 5, '6': 7, '1': 3, '2': 4}

print(j_str)
print(json.dumps(j_str, sort_keys=True, indent=4))
