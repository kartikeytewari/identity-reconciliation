import requests 

identity_link = "http://localhost:5002/identify"
def test_series_1():
    # generate series_2 json object
    contact_send_2_1 = {
        "email": "test_1@gmail.com",
        "phoneNumber": "1"
    }
    
    val = requests.post(identity_link, json=contact_send_2_1)
    val = val.json()
    res_email = val["contact"]["emails"]
    res_phone = val["contact"]["phoneNumbers"]

    assert res_email == ["test_1@gmail.com"]
    assert res_phone == ["1"]

def test_series_2():

    # generate series_1 json object
    contact_send_1_1 = {
        "email": "test_2@gmail.com",
        "phoneNumber": "10"
    }
    contact_send_1_2 = {
        "email": "test_2@gmail.com",
        "phoneNumber": "11"
    }

    requests.post(identity_link, json=contact_send_1_1)
    val = requests.post(identity_link, json=contact_send_1_2)

    val = val.json()
    res_email = val["contact"]["emails"]
    res_phone = val["contact"]["phoneNumbers"]


    assert res_email == ["test_2@gmail.com"]
    assert res_phone == ["10", "11"]
