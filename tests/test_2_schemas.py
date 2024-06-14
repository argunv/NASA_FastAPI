import pytest
from pydantic import ValidationError
from app.schemas import UserCreate, NeoWsCreate, DonkiCreate, TleCreate
from datetime import datetime
import pytz


def test_user_create_schema():
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    user = UserCreate(**user_data)
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_user_create_schema_no_password():
    user_data = {"username": "testuser", "email": "test@example.com"}
    with pytest.raises(ValidationError):
        UserCreate(**user_data)


def test_neows_create_schema():
    neows_data = {"id": 1, "name": "asteroid", "magnitude": 5.6, "is_potentially_hazardous": True}
    neows = NeoWsCreate(**neows_data)
    assert neows.id == 1
    assert neows.name == "asteroid"
    assert neows.magnitude == 5.6
    assert neows.is_potentially_hazardous is True


def test_donki_create_schema():
    donki_data = {
        "activity_id": "12345",
        "start_time": datetime(2022, 1, 1, 0, 0, tzinfo=pytz.UTC),
        "peak_time": datetime(2022, 1, 1, 1, 0, tzinfo=pytz.UTC),
        "end_time": datetime(2022, 1, 1, 2, 0, tzinfo=pytz.UTC),
        "class_type": "solar_flare",
    }
    donki = DonkiCreate(**donki_data)
    assert donki.activity_id == "12345"
    assert donki.start_time.isoformat() == "2022-01-01T00:00:00+00:00"
    assert donki.peak_time.isoformat() == "2022-01-01T01:00:00+00:00"
    assert donki.end_time.isoformat() == "2022-01-01T02:00:00+00:00"
    assert donki.class_type == "solar_flare"


def test_tle_create_schema():
    tle_data = {
        "id": 1,
        "name": "satellite",
        "tle_line1": "1 25544U 98067A   22001.12345678  .00000000  00000-0  00000-0 0  0010",
        "tle_line2": "2 25544  51.6446  74.1234 0007000  90.0000 270.0000 15.48888888220010",
    }
    tle = TleCreate(**tle_data)
    assert tle.id == 1
    assert tle.name == "satellite"
    assert tle.tle_line1 == "1 25544U 98067A   22001.12345678  .00000000  00000-0  00000-0 0  0010"
    assert tle.tle_line2 == "2 25544  51.6446  74.1234 0007000  90.0000 270.0000 15.48888888220010"
