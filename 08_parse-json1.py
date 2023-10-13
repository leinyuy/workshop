import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Buea"
dest = "Limbe"
key = "9cir0GQJhXB2VkUukQDRXTpweVbEeVs8"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)