from app.models import (User, NeoWs, Donki, Tle,
                        get_password_hash, verify_password)


def test_create_user_model():
    user = User(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_create_neows_model():
    neows = NeoWs(name="asteroid", magnitude=5.6, is_potentially_hazardous=True)
    assert neows.name == "asteroid"
    assert neows.magnitude == 5.6
    assert neows.is_potentially_hazardous is True


def test_create_donki_model():
    donki = Donki(activity_id="12345", start_time="2022-01-01 00:00:00", peak_time="2022-01-01 01:00:00",
                  end_time="2022-01-01 02:00:00", class_type="M")
    assert donki.activity_id == "12345"
    assert donki.start_time == "2022-01-01 00:00:00"
    assert donki.peak_time == "2022-01-01 01:00:00"
    assert donki.end_time == "2022-01-01 02:00:00"
    assert donki.class_type == "M"


def test_create_tle_model():
    tle = Tle(name="satellite", tle_line1="1 25544U 98067A   22001.12345678  .00000000  00000-0  00000-0 0  0010",
              tle_line2="2 25544  51.6446  10.7297 0007000  90.0000  90.0000 15.48999999234567")
    assert tle.name == "satellite"
    assert tle.tle_line1 == "1 25544U 98067A   22001.12345678  .00000000  00000-0  00000-0 0  0010"
    assert tle.tle_line2 == "2 25544  51.6446  10.7297 0007000  90.0000  90.0000 15.48999999234567"


def test_verify_password():
    hashed_password = get_password_hash("password123")
    assert verify_password("password123", hashed_password) is True
    assert verify_password("wrongpassword", hashed_password) is False


def test_get_password_hash():
    password = "password123"
    hashed_password = get_password_hash(password)
    assert hashed_password != password
    assert verify_password(password, hashed_password) is True
