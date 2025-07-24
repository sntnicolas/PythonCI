import responses
import requests

@responses.activate
def test_mocked_response():
    responses.add(
        responses.GET,
        'http://example.com/api',
        json={'status': 'ok'},
        status=200
    )

    resp = requests.get('http://example.com/api')
    assert resp.json()['status'] == 'ok'
