def test_get_donki(client):
    response = client.get("/donki/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_neows(client):
    response = client.get("/neows/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_tle(client):
    response = client.get("/tle/?search=A")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_tle(client):
    response = client.get("/tle/1")
    assert response.status_code == 404
    assert response.json() is not None
