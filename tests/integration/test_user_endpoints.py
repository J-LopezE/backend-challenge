import pytest

def test_create_user_returns_201(client, db_setup):
    response = client.post("/api/users/", json={"email": "test@mail.com", "username": "testuser"})
    assert response.status_code == 201
    assert response.json["email"] == "test@mail.com"
    
def test_get_users_returns_200(client, db_setup):
    response = client.get("/api/users/")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    
def test_create_duplicate_user_returns_409(client,db_setup):
     response = client.post("/api/users/", json={"email": "test@mail.com", "username": "testuser"})
     response = client.post("/api/users/", json={"email": "test@mail.com", "username": "testuser"})
     assert response.status_code == 409
