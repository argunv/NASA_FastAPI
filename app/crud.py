from sqlalchemy.orm import Session

from .schemas import UserCreate, UserUpdate, NeoWsCreate, DonkiCreate
from .models import User, Tle, Donki, NeoWs, get_password_hash


def get_user(db: Session, user_id: int) -> User:
    """
    Retrieve a user by user_id.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    """
    Retrieve a user by email.
    """
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> User:
    """
    Retrieve a user by username.
    """
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user.
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate) -> User:
    """
    Update a user.
    """
    db_user = get_user(db, user_id=user_id)
    if db_user:
        if hasattr(user, 'password') and user.password:
            db_user.hashed_password = get_password_hash(user.password)
        db_user.username = user.username
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    """
    Delete a user.
    """
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()


def get_neows(db: Session, neows_id: int) -> NeoWs:
    """
    Retrieve a NeoWs object by neows_id.
    """
    return db.query(NeoWs).filter(NeoWs.id == neows_id).first()


def get_neowses(db: Session, skip: int = 0, limit: int = 100) -> list[NeoWs]:
    """
    Retrieve a list of NeoWs objects with pagination.
    """
    return db.query(NeoWs).offset(skip).limit(limit).all()


def create_neows(db: Session, neows: NeoWsCreate) -> NeoWs:
    """
    Create a new NeoWs object.
    """
    db_neows = NeoWs(id=neows.id,
                     name=neows.name,
                     magnitude=neows.magnitude,
                     is_potentially_hazardous=neows.is_potentially_hazardous)
    db.add(db_neows)
    db.commit()
    db.refresh(db_neows)
    return db_neows


def get_donki(db: Session, donki_id: int) -> Donki:
    """
    Retrieve a Donki object by donki_id.
    """
    return db.query(Donki).filter(Donki.id == donki_id).first()


def get_donkis(db: Session, skip: int = 0, limit: int = 100) -> list[Donki]:
    """
    Retrieve a list of Donki objects with pagination.
    """
    return db.query(Donki).offset(skip).limit(limit).all()


def create_donki(db: Session, donki: DonkiCreate) -> Donki:
    """
    Create a new Donki object.
    """
    db_donki = Donki(activity_id=donki.activity_id,
                     start_time=donki.start_time,
                     peak_time=donki.peak_time,
                     end_time=donki.end_time,
                     class_type=donki.class_type)
    db.add(db_donki)
    db.commit()
    db.refresh(db_donki)
    return db_donki


def get_tle(db: Session, tle_id: int) -> Tle:
    """
    Retrieve a Tle object by tle_id.
    """
    return db.query(Tle).filter(Tle.id == tle_id).first()


def tles_exists(db: Session, id: int) -> bool:
    """
    Check if a Tle object with the given id exists.
    """
    return True if db.query(Tle).filter(Tle.id == id).first() else False


def create_tle(db: Session, tle: Tle) -> Tle:
    """
    Create a new Tle object.
    """
    db_tle = Tle(id=tle.id, name=tle.name, tle_line1=tle.tle_line1, tle_line2=tle.tle_line2)
    db.add(db_tle)
    db.commit()
    db.refresh(db_tle)
    return db_tle
