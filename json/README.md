# JSON in Python

## The basics

To work with JSON in Python, first you need to import JSON. 
To import it you don't have to download anything, you don't have to use pip but you just have to type: 
```python
import json
```

Now you need to load a JSON file or a JSON string, with json.load() and json.loads().

### What is the difference between json.load() and json.loads()?
* json.load() load a JSON file

Example:
```python
import json

#Open file in read only
with open('distros.json', 'r') as json_file:
  #Here load a JSON file
  json_data = json.load(json_file)
```

* json.loads() load a JSON string for a Python file

Example:
```python
import json

json_string = '{ "name":"Gino", "age":19, "city":"New York"}'

#Here load a string in JSON
json_data = json.loads(json_string)
```

## How to read data

Now we need to read the data from the JSON file/string.

For this we have to do json_data['entry'] 

Example:
* The JSON file:
```json
{
  "how_many_distros": 3,
  "distros": [
      {
          "distro_name": "Ubuntu",
          "based_on": "Debian",
          "default_de": "Gnome"
      },
      {
          "distro_name": "Linux Mint",
          "based_on": "Ubuntu",
          "default_de": "Cinnamon"
      },
      {
          "distro_name": "EnsoOS",
          "based_on": "Ubuntu",
          "default_de": "Xfce"
      }
  ]
}
```
* The Python file:
```python
import json
  
#Open file in read only
with open('distros.json', 'r') as json_file:
  #Here load a JSON file
  json_data = json.load(json_file)
  #Here grab the entry of the JSON file and writes it
  print(json_data['how_many_distros'])
  #Output: 3
```
  
## How to read a JSON array
For read a JSON array we need to write json_data['array_name'][array_number]['entry']
  
* Python file:
```python
import json
  
#Open file in read only
with open('distros.json', 'r') as json_file:
  #Here load a JSON file
  json_data = json.load(json_file)
  #Here grab the entry of an array in the JSON file and writes it
  print(json_data['distros'][0]['distro_name'])
  #Output: Ubuntu
```
  
