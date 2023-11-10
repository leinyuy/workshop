import requests
import json

choice=input("Do you want to use the hard-coded access token?(y/n)? ")

if choice == "n" or choice== "N":
    accessToken = input("Please enter your access token. ")
    accessToken = "Bearer " + accessToken
else:
    accessToken = "Bearer YzA2MWE1OWMtMTQ3Mi00OGExLTgwOGUtOTA0NDM4YmFiMGViMTEyZmE3OWYtZTc0_PE93_8419c701-37c9-4dbf-b218-12dcd2362fa6"


# step 2
apiUri = "https://api.ciscospark.com/v1/rooms" 
resp = requests.get( apiUri, 
                     headers = {"Authorization":accessToken}
                   ) 
if not resp.status_code == 200:
    raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))

json_data = resp.json()

print("Webex Teams Response Data:") # Print identifying string
print( json.dumps(json_data, indent = 4) )