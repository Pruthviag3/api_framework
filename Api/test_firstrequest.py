import pytest
import requests

def test_getrequest_validateion():

    base_url="https://reqres.in"

    header={
        'Content-Type': 'application/json'
    }

    response=requests.get(url=base_url + "/api/users/2",headers=header,verify=False)
    assert response.status_code==200
    print(response.json())