import json


def test_create_device(client):
    data = {
        "company": "Biotronik",
        "company_url": "www.biotronik.com",
        "make": "Entovis",
        "model": "entdrt",
        "device_type": "ppm"
        }
    response = client.post("/devices/create-device/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "Biotronik"
    assert response.json()["make"] == "Entovis"


def test_read_device(client):
    data = {
        "company": "doogle",
        "company_url": "www.biotronik.com",
        "make": "Entovis",
        "model": "entdrt",
        "device_type": "ppm"
        }
    response = client.post("/devices/create-device/", json.dumps(data))

    response = client.get("/devices/get/1/")
    assert response.status_code == 200
    assert response.json()['make'] == "Entovis"