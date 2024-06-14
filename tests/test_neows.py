def test_get_neows(client):
    response = client.get("/neows/")
    assert response.status_code == 200
    assert len(response.json()) > 0
