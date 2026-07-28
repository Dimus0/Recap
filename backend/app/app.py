from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models.models  # noqa: F401 — register all ORM mappers


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Recap",
    lifespan=lifespan,
    swagger_ui_parameters={"persistAuthorization": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
