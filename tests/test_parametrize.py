import pytest
import requests

@pytest.mark.parametrize(
    "endpoint, expected_status",
    [
        ("/users", 200),
        ("/posts", 200),  # fake
        ("/posts", 201),
        ("/invalid-endpoint", 404),
    ]
)
def test_api_status_codes(endpoint, expected_status):
    base_url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{base_url}{endpoint}", timeout=5)
    assert response.status_code == expected_status
