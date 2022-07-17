from fastapi.testclient import TestClient

from app.kvstore import app

client = TestClient(app) 

def test_set_correct_format():
    """
    To test the response status code
    when provided with well formated input
    """
    res = client.post("/set",json={"key": "1","value": "1"})
    print(res.json())
    assert res.status_code == 200


def test_set_bad_format():
    """
    To test the response status code
    when provided with bad format
    """
    res = client.post("/set",json={"key":1})
    print(res.json())
    assert res.status_code == 422


def test_set_with_data_in_db():
    """
    To test the output
    when provided with existing key
    """
    res = client.post("/set",json={"key": "test-key","value": "test-value"})
    print(res.json())
    value = client.get("/get/test-key")
    expected_output = "test-value"
    output = value.json()
    assert output == expected_output

