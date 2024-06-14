from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import httpx
from app.crud import create_neows
from app.schemas import NeoWs, NeoWsCreate
from app.dependencies import get_db
from app.config import NASA_API_KEY, NEO_URL

import app.models as models


router = APIRouter()


@router.get("/", response_model=list[NeoWs])
def get_neows(db: Session = Depends(get_db)) -> list[NeoWs]:
    """Retrieve Near Earth Object Web Service (NeoWs) data from NASA API.

    Args:
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        list[NeoWs]: A list of NeoWs objects representing the retrieved NEO data.
    """
    with httpx.Client() as client:
        response = client.get(f"{NEO_URL}?api_key={NASA_API_KEY}")
    data = response.json()

    neows_list = []

    for date in data.get("near_earth_objects", {}):
        for item in data["near_earth_objects"][date]:
            neows = NeoWsCreate(
                id=item["id"],
                name=item["name"],
                magnitude=item["absolute_magnitude_h"],
                is_potentially_hazardous=bool(item["is_potentially_hazardous_asteroid"])
            )
            existing_neows = db.query(models.NeoWs).filter(models.NeoWs.id == neows.id).first()
            if existing_neows:
                neows_list.append(existing_neows)
                continue
            obj = create_neows(db, neows)
            neows_list.append(obj)

    return neows_list
