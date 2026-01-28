"""System endpoints."""
import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Get path to 'templates' folder relative to this file
current_dir = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(current_dir, "..", "templates")
templates = Jinja2Templates(directory=template_path)

@router.get("/health", response_class=HTMLResponse)
async def get_health(request: Request):
    """Health check endpoint."""
    return templates.TemplateResponse("index.html", {"request": request})
