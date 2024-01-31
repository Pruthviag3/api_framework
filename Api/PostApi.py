import requests

header = {
    'Accept':'text/plain',
'Content-Type': 'application/json'
}

request_payload = {

  "id": 311,
  "idBook": 3421,
  "firstName": "abc",
  "lastName": "xyz"

}

response =requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=header,json=request_payload)
print(response.status_code)
print(response.json())

data=response.json()
print(data['id'])
assert response.status_code == 200
assert data['id']== 311
