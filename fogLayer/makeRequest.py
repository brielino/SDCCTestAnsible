# importing the requests library
import json

import requests

# api-endpoint
URL = "https://aj39eevcx6.execute-api.us-east-2.amazonaws.com/Development/sayhello"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address' :location}
header = {'authToken': 'allow'}
# sending get request and saving the response as response object
r = requests.get(url = URL,headers=header)
# extracting data in json format
#data = json.dumps(r.json())
#res = json.loads(data)
print("Response Code: " , r.status_code)
if r.status_code == 200:
    res = json.loads(r.content)
    body = json.loads(res["body"])
    print("Lat: " , body["lat"])
    print("Lat: " , body["long"])



