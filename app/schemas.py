from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    """
    Base model for user data.
    """
    username: str
    email: str


class UserCreate(UserBase):
    """
    Model for creating a new user.
    """
    password: str


class User(UserBase):
    """
    Model for user data.
    """
    id: int

    class Config:
        """
        Pydantic configuration for User model.
        """
        from_attributes = True


class UserUpdate(UserBase):
    """
    Model for updating user data.
    """
    pass


class NeoWsBase(BaseModel):
    """
    Base model for Near Earth Object Web Service data.
    """
    id: int
    name: str
    magnitude: float
    is_potentially_hazardous: bool


class NeoWsCreate(NeoWsBase):
    """
    Model for creating a new Near Earth Object Web Service data.
    """
    pass


class NeoWs(NeoWsBase):
    """
    Model for Near Earth Object Web Service data.
    """
    id: int

    class Config:
        """
        Pydantic configuration for NeoWs model.
        """
        from_attributes = True


class DonkiBase(BaseModel):
    """
    Base model for Space Weather Database Of Notifications, Knowledge, Information (DONKI) data.
    """
    activity_id: str
    start_time: datetime
    peak_time: datetime
    end_time: datetime
    class_type: str


class DonkiCreate(DonkiBase):
    """
    Model for creating a new Space Weather Database Of Notifications, Knowledge, Information (DONKI) data.
    """
    pass


class Donki(DonkiBase):
    """
    Model for Space Weather Database Of Notifications, Knowledge, Information (DONKI) data.
    """
    id: int

    class Config:
        """
        Pydantic configuration for Donki model.
        """
        from_attributes = True


class TleBase(BaseModel):
    """
    Base model for Two-Line Elements (TLE) data.
    """
    id: int
    name: str
    tle_line1: str
    tle_line2: str


class TleCreate(TleBase):
    """
    Model for creating a new Two-Line Elements (TLE) data.
    """
    pass


class Tle(TleBase):
    """
    Model for Two-Line Elements (TLE) data.
    """
    id: int

    class Config:
        """
        Pydantic configuration for Tle model.
        """
        from_attributes = True
