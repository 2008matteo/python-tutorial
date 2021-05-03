import json

#Open file in read only
with open('ubuntu_distro.json', 'r') as json_file:
    #Here load a JSON file
    json_data = json.load(json_file)
    #Print a data from JSON
    print(json_data['distro_name'])