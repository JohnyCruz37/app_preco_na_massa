from fastapi import FastAPI
from app.database.database import engine
from app.models.user import Base
from app.routers import router as app_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(app_router)