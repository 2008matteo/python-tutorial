# JSON in Python

  To work with JSON in Python, first you need to import JSON. 
  To import it you don't have to download anything, you don't have to use pip but you just have to type: 
  ```python
  import json
  ```
  
  ## What is the difference between json.load() and json.loads()?
  * json.load() load a JSON file.

  Example:
  ```python
  import json
  
  with open('distros.json', 'r') as json_file:
    #Here load a JSON file
    json_data = json.load(json_file)
  ```

  * json.loads() load a JSON string for a Python File

  Example:
  ```python
  import json
  
  json_string = '{ "name":"Gino", "age":19, "city":"New York"}'
  
  #Here load a string in JSON
  json_data = json.loads(json_string)
  ```
  
