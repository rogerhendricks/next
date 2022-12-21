import uvicorn
from fastapi import FastAPI
from core.config import settings
from fastapi.staticfiles import StaticFiles
from apis.base import api_router
from db.session import engine
from db.base import Base


def configure_static(app):
	app.mount("/static", StaticFiles(directory="static"), name="static")


def include_router(app):
	app.include_router(api_router)


def create_tables():
	print("create_tables")#new
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()
	return app


app = start_application()

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0" , port=8000, log_level="info", reload="true")