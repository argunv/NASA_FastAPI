from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import declarative_base
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base = declarative_base()


class User(Base):
    """
    Represents a user in the system.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)


class NeoWs(Base):
    """
    Represents a Near Earth Object in the system.
    """
    __tablename__ = 'neows'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    magnitude: float = Column(Float)
    is_potentially_hazardous: bool = Column(Boolean)


class Donki(Base):
    """
    Represents a space weather event in the system.
    """
    __tablename__ = 'donki'

    id: int = Column(Integer, primary_key=True, index=True)
    activity_id: str = Column(String)
    start_time: DateTime = Column(DateTime)
    peak_time: DateTime = Column(DateTime)
    end_time: DateTime = Column(DateTime)
    class_type: str = Column(String)


class Tle(Base):
    """
    Represents a Two-Line Element Set in the system.
    """
    __tablename__ = 'tle'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    tle_line1: str = Column(String)
    tle_line2: str = Column(String)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify if the plain password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Generate a hashed password from the given plain password.
    """
    return pwd_context.hash(password)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from config import DATABASE_URL

    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
