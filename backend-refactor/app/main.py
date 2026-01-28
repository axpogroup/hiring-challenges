"""Main entry point for the application."""
import uvicorn

from app.core.config import get_settings
from app.core.logging import setup_logging
from app.factory import create_app

settings = get_settings()
setup_logging(settings.log_level)

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=settings.debug_mode 
    )
