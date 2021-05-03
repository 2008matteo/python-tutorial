import json
  
json_string = '{"how_many_distros": 3, "distros": [ { "distro_name": "Ubuntu", "based_on": "Debian", "default_de": "Gnome" }, { "distro_name": "Linux Mint", "based_on": "Ubuntu", "default_de": "Cinnamon" }, { "distro_name": "EnsoOS", "based_on": "Ubuntu", "default_de": "Xfce"}]}'
  
#Here load a string in JSON
json_data = json.loads(json_string)
print(print(json_data['distros'][0]['distro_name']))