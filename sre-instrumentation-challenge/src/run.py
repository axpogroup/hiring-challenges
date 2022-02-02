import os

from storage import app
from waitress import serve

if __name__ == "__main__":
    port = os.getenv("PORT", default=5000)
    serve(app, host="0.0.0.0", port=port)
