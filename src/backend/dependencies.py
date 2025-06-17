# src/backend/dependencies.py
from src.backend.database import SessionLocal
from sqlalchemy.orm import Session

# Dependency to be used in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()