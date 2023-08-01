import requests

# Read he data from the excel file
# Pass the data one by one and run tst_make_auth_request, how many row in the excel zffile



def test_make_auth_request():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    # tO verify that Expected Result == Actual Result
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])
