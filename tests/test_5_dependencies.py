from app.dependencies import get_db, SessionLocal


def test_get_db():
    db = next(get_db())
    assert db is not None
    db.close()


def test_get_db_multiple_times():
    db1 = next(get_db())
    db2 = next(get_db())
    assert db1 is not None
    assert db2 is not None
    assert db1 != db2
    db1.close()
    db2.close()


def test_get_db_context_manager():
    with next(get_db()) as db:
        assert db is not None
        db.close()


def test_get_db_context_manager_multiple_times():
    with next(get_db()) as db1:
        assert db1 is not None
        with next(get_db()) as db2:
            assert db2 is not None
            assert db1 != db2


def test_get_db_session_local():
    db = SessionLocal()
    assert db is not None
    db.close()


def test_get_db_session_local_multiple_times():
    db1 = SessionLocal()
    db2 = SessionLocal()
    assert db1 is not None
    assert db2 is not None
    assert db1 != db2
    db1.close()
    db2.close()
