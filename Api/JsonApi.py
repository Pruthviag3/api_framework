import requests
import json

base_url="https://reqres.in/api/users"
head={
    'Content-Type': 'application/json'
}

json_file=open('./users.json')
json_payload=json.load(json_file)

response=requests.post(url=base_url,headers=head,json=json_payload,verify=False)
print(response.status_code)
print(response.text)
