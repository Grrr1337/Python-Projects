import os
from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=(Path(__file__).parent.parent / "frontend"))


def sample_webpage(request: Request):
    # Pass the user_activities to the HTML template for rendering
    return templates.TemplateResponse(
        "sample_webpage.html", {"request": request, "message": "sample_webpage"}
    )
