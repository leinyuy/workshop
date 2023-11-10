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

jsonData = resp.json()

messages = jsonData["items"]
messageText = input("What text are you searching for? ")
messageCounter=0

for message in messages:
    if message["text"].find(messageText) != -1:
        # Student Step #3b: Following this comment, increment message counter variable by 1
        messageCounter+=1
        
        messageId = message["id"]
        print("Found a message with: " + messageText)
        print("Message: " + message["text"])
        print("Email Address of the Message Creator: " + message["personEmail"])

        
        print("Date/Time the Message was Created: " + message["created"])
        print(messageCounter)
        print("Message: " + message["text"])
        
# if messageCounter >0:

    # <!!!REPLACEME with print function printing the number of found messages!!!>


# print("Thank you for using this program and think API + Python!")




