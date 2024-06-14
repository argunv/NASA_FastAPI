from fastapi import FastAPI
from .models import Base
from .dependencies import engine
from app.routes import users, neows, donki, tle


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, tags=["Users"])
app.include_router(neows.router, prefix="/neows", tags=["NeoWs"])
app.include_router(donki.router, prefix="/donki", tags=["Donki"])
app.include_router(tle.router, prefix="/tle", tags=["Tle"])
