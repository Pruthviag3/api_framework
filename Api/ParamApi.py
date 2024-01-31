import requests

para = {
    'page':2,
    'per_page':1
}
url="https://gorest.co.in/public/v2/users"
response = requests.get(url,params=para,verify=False)
print(response.json())
assert response.status_code==200