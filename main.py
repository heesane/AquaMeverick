from fastapi import FastAPI,Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime
app = FastAPI()

@app.get("/")
async def root():
    return "Team : Aqua Mavericks"