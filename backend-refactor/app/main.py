"""Main entry point for the application."""
import uvicorn
from helpers.startup import startup
from app import create_app


app = create_app()
startup(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
