from fastapi.testclient import TestClient

from app.kvstore import app

client = TestClient(app) 

def test_search_empty_query():
    """
    To test the response status code
    when provided with empty query
    """
    res = client.get("/search")
    print(res.json())
    assert res.status_code == 200


def test_output_search_empty_query():
    """
    To test the output
    when provided with  empty query
    """
    res = client.get("/search")
    print(res.json())
    expected_output = []
    output=res.json()
    assert expected_output == output


def test_output_search_with_query1():
    """
    To test the response status code
    when provided with query
    """
    res = client.get("/search?prefix=abc")
    print(res.json())
    expected_output = ['abc-1','abc-2']
    output = res.json()
    assert output == expected_output

def test_output_search_with_query2():
    """
    To test the response status code
    when provided with query
    """
    res = client.get("/search?suffix=-1")
    print(res.json())
    expected_output = ['abc-1','xyz-1']
    output = res.json()
    assert output == expected_output