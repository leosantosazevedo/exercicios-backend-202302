import requests
import json
import pprint
import yaml

api_key = "xxxxx"
nome_da_cidade = "Rio de Janeiro"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + nome_da_cidade

print(complete_url)
response = requests.get(complete_url)
x = response.json()
#pprint.pprint(x)
ymal_string=yaml.dump(x)
print("The YAML string is:")
print(ymal_string)

y = x["main"]
current_temp = y["temp"]
print(current_temp)