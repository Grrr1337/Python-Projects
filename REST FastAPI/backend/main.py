
# To run locally use:
# .venv\Scripts\Activate     ### <- for a Windows machine
# cd autocad-backend/backend/
# uvicorn main:app --reload
import time
from datetime import datetime, timedelta
from typing import Annotated, Dict, Optional
import uvicorn
from fastapi import Body, Cookie, FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import Info, Tag
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER, HTTP_307_TEMPORARY_REDIRECT
import os
from pathlib import Path
from webpage_requests_handler import sample_webpage

app = FastAPI(
    title="REST FastAPI",
    description="Sample REST FastAPI Server",
    version="1.0.0",
    openapi_tags=[
        Tag(name="Main", description="User maintainance functionalty"),
        Tag(
            name="Webpages",
            description="Additional Web frontend endpoints",
        ),
    ],
    info=Info(
        title="REST FastAPI",
        description="Sample REST Server",
        version="1.0.0",
    ),
)


@app.get(
    "/",
    tags=["Main"],
    summary="Root",
)
async def read_root():
    return {"message": "Navigate to /docs"}



# region frontend webpages
app.mount(
    "/static",
    StaticFiles(directory=(Path(__file__).parent.parent / "frontend/static")),
    name="static",
)


@app.get(
    "/sample_webpage",
    tags=["Webpages"],
    summary="Navigates to a sample webpage",
    response_class=HTMLResponse,
)
async def handler_sample_webpage(
    request: Request, token: Annotated[str | None, Cookie()] = None
):
    return sample_webpage(request)
# endregion frontend webpages


if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
