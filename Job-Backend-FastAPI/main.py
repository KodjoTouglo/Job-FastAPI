from fastapi import FastAPI

from api.base import api_router

from core.config import settings

from data.session import engine
from data.base import Base

from models.jobs import Job
from models.users import User


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(api_router)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}
