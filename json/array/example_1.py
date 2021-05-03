import json
  
#Open file in read only
with open('distros.json', 'r') as json_file:
    #Here load a JSON file
    json_data = json.load(json_file)
    print(json_data['distros'][0]['distro_name'])