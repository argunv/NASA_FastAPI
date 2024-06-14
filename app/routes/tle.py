from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import httpx
from app.crud import create_tle, tles_exists, get_tle
from app.schemas import Tle, TleCreate
from app.dependencies import get_db
from app.config import TLE_URL

router = APIRouter()


@router.get("/", response_model=list[Tle])
def search_tle_by_name(search: str, db: Session = Depends(get_db)) -> list[Tle]:
    """Search TLE by name.

    Args:
        search (str): The search string used to filter the TLE data by name.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        list[Tle]: A list of Tle objects that match the search criteria.

    Raises:
        ReadTimeout: If a read timeout occurs while making the HTTP request.
        Exception: If any other error occurs during the execution of the function.
    """
    try:
        with httpx.Client(follow_redirects=True) as client:
            response = client.get(TLE_URL, timeout=30)
        data = response.json()

        tle_list = []
        for item in data.get('member', []):
            if search in item['name']:
                existing_tle = tles_exists(db, id=item['satelliteId'])

                tle = TleCreate(
                    id=item['satelliteId'],
                    name=item['name'],
                    tle_line1=item['line1'],
                    tle_line2=item['line2']
                )

                if existing_tle:
                    obj = get_tle(db, tle.id)
                    tle_list.append(obj)
                else:
                    obj = create_tle(db, tle)
                    tle_list.append(obj)

        return tle_list

    except httpx.ReadTimeout as e:
        print(f"Read timeout error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


@router.get("/{q}", response_model=Tle)
def get_tle_by_id(q: int, db: Session = Depends(get_db)) -> Tle:
    """Get TLE by ID.

    Retrieves the TLE (Two-Line Elements) data for a satellite with the specified ID.

    Args:
        q (int): The ID of the satellite.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        Tle: The Tle object containing the satellite's TLE data.

    Raises:
        HTTPException: If the request to retrieve the data fails or if the response cannot be parsed as JSON.

    """
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(f"{TLE_URL}/{q}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve data")
    try:
        data = response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to parse response as JSON")

    existing_tle = tles_exists(db, id=data['satelliteId'])

    tle = TleCreate(
        id=data['satelliteId'],
        name=data['name'],
        tle_line1=data['line1'],
        tle_line2=data['line2']
    )

    if not existing_tle:
        create_tle(db, tle)

    return tle
