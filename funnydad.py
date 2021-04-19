import requests
import json
from pprint import pprint

url = "http://api.icndb.com/jokes/random"

payload={}
headers = {
           'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

cn_response_json = response.json()

print("What are the chances of this being a dirty joke?")
pprint(cn_response_json)

