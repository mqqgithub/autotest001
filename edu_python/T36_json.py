import json
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_data = json.dumps(data)
print(type(json_data), json_data)

python_data = json.loads(json_data)
print(type(python_data), python_data)


