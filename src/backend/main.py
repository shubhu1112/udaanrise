from fastapi import FastAPI
from src.backend.routes import auth
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ Allow frontend to access backend (from browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify frontend URL here for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
