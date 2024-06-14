def test_get_donki(client):
    response = client.get("/donki/")
    assert response.status_code == 200
    assert len(response.json()) > 0
