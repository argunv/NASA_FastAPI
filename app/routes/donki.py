from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import httpx
from app.crud import create_donki
from app.schemas import Donki, DonkiCreate
from app.dependencies import get_db
from app.config import NASA_API_KEY, DONKI_URL

import app.models as models


router = APIRouter()


@router.get("/", response_model=list[Donki])
def get_donki(db: Session = Depends(get_db)) -> list[Donki]:
    """Retrieve DONKI data from NASA API and store it in the database.

    Args:
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        list[Donki]: A list of Donki objects stored in the database.
    """
    with httpx.Client() as client:
        response = client.get(f"{DONKI_URL}?api_key={NASA_API_KEY}")
    data = response.json()

    donki_list = []
    for item in data:
        activity_id = None
        if item['linkedEvents'] and isinstance(item['linkedEvents'], list):
            for event in item['linkedEvents']:
                if 'activityID' in event:
                    activity_id = event['activityID']
                    break
        if not activity_id:
            continue

        # Check if donki with the same activity_id already exists in the database
        existing_donki = db.query(models.Donki).filter(models.Donki.activity_id == str(activity_id)).first()
        if existing_donki:
            donki_list.append(existing_donki)
        else:
            donki = DonkiCreate(
                activity_id=str(activity_id),
                start_time=item['beginTime'],
                peak_time=item['peakTime'],
                end_time=item['endTime'],
                class_type=item['classType']
            )
            obj = create_donki(db, donki)
            donki_list.append(obj)

    return donki_list
