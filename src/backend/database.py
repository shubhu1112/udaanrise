import os
from pathlib import Path
from dotenv import load_dotenv

# ✅ Load the .env file from current directory
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# ✅ Now load the DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")
print("DEBUG: DATABASE_URL =", DATABASE_URL)  # ← required to confirm it's working

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr



engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
