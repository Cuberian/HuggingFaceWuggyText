from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"result": "error",
                               "message": "add 'q' parameter to request"}


def test_read_main_params():
    response = client.get("/?q=keanu")
    assert response.status_code == 200
    answer = response.json()
    assert answer["result"] == 'success'
    assert 'Keanu Reeves' in answer["data"]


def test_check_not_found_articles():
    response = client.get('/?q="     "')
    assert response.status_code == 200
    assert response.json() == {"result": "success",
                               "message": "0 articles waw found"}


def test_ask_keanu():
    response = client.get("/ask?title=Keanu%20Reeves&question=how%20is"
                          "%20Keanu%20Reeves")
    assert response.status_code == 200
    assert response.json()["data"]["answer"] == " \"absolutely charismatic"
