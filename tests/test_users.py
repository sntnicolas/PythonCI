# test_users.py

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# test_users.py
def test_users_status_code(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
