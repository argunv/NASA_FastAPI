from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import crud
from app.main import app
from app.schemas import UserUpdate, NeoWsCreate, DonkiCreate, TleCreate


client = TestClient(app)

JSON_USER_TEST = {
    "username": "test9user",
    "email": "test9@example.com",
    "password": "test9password"
}
TEST_DONKI_DATA = {
    "activity_id": "2016-01-15T00:00:00",
    "start_time": "2022-01-01 00:00:00",
    "peak_time": "2022-01-01 01:00:00",
    "end_time": "2022-01-01 02:00:00",
    "class_type": "M"
}
TEST_NEOWS_DATA = {
    "id": 1,
    "name": "asteroid",
    "magnitude": 5.6,
    "is_potentially_hazardous": True
}
TEST_TLE_DATA = {
    "id": 1,
    "name": "satellite",
    "tle_line1": "1 25544U 98067A   22001.12345678  .00000000  00000-0  00000-0 0  0010",
    "tle_line2": "2 25544  51.6446  74.1234 0007000  90.0000 270.0000 15.48888888220010"
}


def test_create_user(client):
    response = client.post("/users/", json=JSON_USER_TEST)
    global test_user_id
    test_user_id = response.json()["id"]
    assert response.status_code == 200


def test_get_user(db: Session):
    user = crud.get_user(db, user_id=test_user_id)
    assert user is not None


def test_get_user_by_email(db: Session):
    user = crud.get_user_by_email(db, email="test9@example.com")
    assert user is not None


def test_get_user_by_username(db: Session):
    user = crud.get_user_by_username(db, username="test9user")
    assert user is not None


def test_update_user(db: Session):
    user_data = UserUpdate(username="test9updateduser", email="test9updated@example.com")
    user = crud.update_user(db, user_id=test_user_id, user=user_data)
    assert user is not None
    assert user.username == "test9updateduser"
    assert user.email == "test9updated@example.com"


def test_delete_user(db: Session):
    crud.delete_user(db, user_id=test_user_id)
    user = crud.get_user(db, user_id=test_user_id)
    assert user is None


def test_create_neows(db: Session):
    neows_data = NeoWsCreate(**TEST_NEOWS_DATA)
    neows = crud.create_neows(db, neows=neows_data)
    assert neows is not None


def test_get_neows(db: Session):
    neows = crud.get_neows(db, neows_id=TEST_NEOWS_DATA["id"])
    assert neows is not None


def test_get_neowses(db: Session):
    neows_list = crud.get_neowses(db, skip=0, limit=10)
    assert len(neows_list) > 0


def test_create_donki(db: Session):
    donki_data = DonkiCreate(**TEST_DONKI_DATA)
    donki = crud.create_donki(db, donki=donki_data)
    assert donki is not None


def test_get_donki(db: Session):
    donki = crud.get_donki(db, donki_id=1)
    assert donki is not None


def test_get_donkis(db: Session):
    donki_list = crud.get_donkis(db, skip=0, limit=10)
    assert len(donki_list) > 0


def test_create_tle(db: Session):
    tle_data = TleCreate(**TEST_TLE_DATA)
    tle = crud.create_tle(db, tle=tle_data)
    assert tle is not None


def test_get_tle(db: Session):
    tle = crud.get_tle(db, tle_id=TEST_TLE_DATA["id"])
    assert tle is not None


def test_tles_exists(db: Session):
    exists = crud.tles_exists(db, id=1)
    assert exists is True
