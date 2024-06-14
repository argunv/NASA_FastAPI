from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app import crud, schemas, dependencies

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    """Create a new user.

    Args:
        user (schemas.UserCreate): User data to be created.
        db (Session, optional): Database session. Defaults to Depends(dependencies.get_db).

    Returns:
        schemas.User: Created user data.

    Raises:
        HTTPException: If email or username is already registered.
        HTTPException: If something went wrong during user creation.
    """
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    elif crud.get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    try:
        return crud.create_user(db=db, user=user)
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong!")


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    """Read user data by user ID.

    Args:
        user_id (int): User ID.
        db (Session, optional): Database session. Defaults to Depends(dependencies.get_db).

    Returns:
        schemas.User: User data.

    Raises:
        HTTPException: If user is not found.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=schemas.UserUpdate)
def update_user(user_id: int,
                user: schemas.UserUpdate,
                db: Session = Depends(dependencies.get_db)) -> schemas.UserUpdate:
    """Update user data by user ID.

    Args:
        user_id (int): User ID.
        user (schemas.UserUpdate): Updated user data.
        db (Session, optional): Database session. Defaults to Depends(dependencies.get_db).

    Returns:
        schemas.UserUpdate: Updated user data.

    Raises:
        HTTPException: If user is not found.
    """
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    """Delete user data by user ID.

    Args:
        user_id (int): User ID.
        db (Session, optional): Database session. Defaults to Depends(dependencies.get_db).

    Returns:
        schemas.User: Deleted user data.

    Raises:
        HTTPException: If user is not found.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id=db_user.id)
    return Response(status_code=200)
