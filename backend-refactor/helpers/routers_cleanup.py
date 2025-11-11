
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# Setup templates
templates = Jinja2Templates(directory="templates")

def cleanup(router):
    @router.get("/health", response_class=HTMLResponse) # type: ignore
    async def get_health(request: Request):
        """Health check endpoint."""
        return templates.TemplateResponse("index.html", {"request": request})