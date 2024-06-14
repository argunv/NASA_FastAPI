JSON_USER_TEST = {
    "username": "testuser_one",
    "email": "test_email@example.com",
    "password": "testpassword"
}


def test_create_user(client):
    response = client.post("/users/", json=JSON_USER_TEST)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser_one"
    global user_id
    user_id = response.json()["id"]


def test_read_user(client):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser_one"


def test_update_user(client):
    response = client.put(f"/users/{user_id}", json={"username": "updateduser", "email": "updated@example.com"})
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"


def test_delete_user(client):
    print(user_id)
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
