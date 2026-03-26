import requests
import pytest

# Test to check if the choosen city returns 200 status code
def test_get_weather_success(api_config):
    city = "Melbourne"
    params = {
        "q": city,
        "appid": api_config["key"]
    }
    response = requests.get(api_config["url"], params=params)
    assert response.status_code == 200
    assert response.json()["name"] == city

    # Test 2 to check multiple cities at once
def test_get_weather_multiple_cities(api_config):
    cities = ["Sydney", "Brisbane", "Perth", "Adelaide", "Darwin"]
    for city in cities:
        params = {
            "q": city,
            "appid": api_config["key"]
        }
        response = requests.get(api_config["url"], params=params)
        assert response.status_code == 200
        assert response.json()["name"] == city
    
    # Test 3 to check negative test 401 status code for invalid API key
def test_get_weather_invalid_api_key(api_config):
    city = "Melbourne"
    params = {
        "q": city,
        "appid": "invalid_key"
    }
    response = requests.get(api_config["url"], params=params)
    assert response.status_code == 401