from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int    
    email: EmailStr


    class Config:
        from_attributes = True  # Pydantic v2


