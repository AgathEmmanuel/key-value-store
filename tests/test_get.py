from fastapi.testclient import TestClient

from app.kvstore import app

client = TestClient(app) 

def test_get_not_existing_key():
    """
    To test the response status code
    when provided with not existing key
    """
    res = client.get("/get/zzz")
    print(res.json())
    assert res.status_code == 404


def test_get_existing_key():
    """
    To test the response status code
    when provided with existing key
    """
    res = client.get("/get/abc-1")
    print(res.json())
    assert res.status_code == 200