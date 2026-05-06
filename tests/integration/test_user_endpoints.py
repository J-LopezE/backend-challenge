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

def test_get_user_by_id_returns_200(client, db_setup):
    client.post("/api/users/", json={"email": "test@mail.com", "username": "test"})
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json["id"] == 1


def test_update_user_returns_200(client, db_setup):
    client.post("/api/users/", json={"email": "test@mail.com", "username": "test"})
    response = client.put("/api/users/1", json={"email": "updated@mail.com"})
    assert response.status_code == 200
    assert response.json["email"] == "updated@mail.com"


def test_delete_user_returns_200(client, db_setup):
    client.post("/api/users/", json={"email": "test@mail.com", "username": "test"})
    response = client.delete("/api/users/1")
    assert response.status_code == 200