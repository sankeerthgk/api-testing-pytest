import requests
import pytest

@pytest.fixture()
def api_response():
    url = 'http://api.zippopotam.us/us/90210'
    response = requests.get(url)
    return response

@pytest.fixture()
def api_response_body_json(api_response):
    print(api_response.json())
    return api_response.json()

def test_status_code(api_response):
    print('status_code of response is:' + str(api_response.status_code))
    assert 200 == api_response.status_code

def test_zipcode(api_response_body_json):
    zip_code = api_response_body_json['post code']
    print('Zipcode value is:' + zip_code)
    assert 90210 == int(zip_code)

def test_place_name(api_response_body_json):
    place_name = api_response_body_json['places'][0]['place name']
    print('Zipcode value is:' + place_name)
    assert 'Beverly Hills' == place_name