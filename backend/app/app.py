from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent))

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    yield

app = FastAPI(
    title="Recap",
    swagger_ui_parameters={"persistAuthorization": True}, 
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # адреса майбутнього React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)