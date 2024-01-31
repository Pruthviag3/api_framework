import requests

head = {
'Content-Type': 'application/json',
'Authorization' : 'Bearer 0635faf7625273e45fefeb30cf9d38c8699c31dc168d2851afb0852a70b28688'
}

body = {

    "name": "Bilva Dhawanhello",
    "email": "bilva_dhawanhello12567@okon-altenwerth.test",
    "gender": "female",
    "status": "inactive"
}
url="https://gorest.co.in/public/v2/users/"
response =requests.post(url,headers=head,json=body,verify=False)
print(response.json())
assert response.status_code==201

getresponse = requests.get(url + str(response.json()['id']),headers=head,verify=False)
print(getresponse.json())
