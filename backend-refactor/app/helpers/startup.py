from services import measurement_legacy
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

def startup(app):   
    # Mount static files
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(measurement_legacy.router, tags=["measurements"])