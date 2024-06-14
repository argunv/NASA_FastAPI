from app.database import SessionLocal


def test_database_connection():
    session = SessionLocal()
    try:
        assert session is not None
    finally:
        session.close()
