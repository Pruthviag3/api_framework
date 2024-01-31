import requests

head = {
    'Accept': 'text/plain'
}


response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Books/311",headers=head)
print("Before Put")
print(response.json())

header = {
    'Accept':'text/plain',
'Content-Type': 'application/json'
}

putPayload = {

  "id": 333,
  "title": "Hi",
  "description": "string",
  "pageCount": 0,
  "excerpt": "string",
  "publishDate": "2023-10-26T07:29:06.196Z"

}
reponse_Put= requests.put("https://fakerestapi.azurewebsites.net/api/v1/Books/311",headers=header,json=putPayload)
print(reponse_Put.json())

assert reponse_Put.status_code==200

