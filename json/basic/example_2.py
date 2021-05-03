import json

json_string = '{ "name":"Gino", "age":19, "city":"New York"}'

#Here load a string in JSON
json_data = json.loads(json_string)

#Print a data from JSON
print(json_data['name'])