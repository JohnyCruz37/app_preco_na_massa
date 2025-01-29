from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    celular: str = Field(..., pattern=r'^\d{11}$')
    senha: str
    pro_labore: Optional[float] = None

class UserInDB(UserCreate):
    idUsuario: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class UserResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True

class UserDeleteResponse(BaseModel):
    message: str