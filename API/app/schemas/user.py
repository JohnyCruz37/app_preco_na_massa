from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    celular: str = Field(..., pattern=r'^\+[1-9]\d{1,14}$')
    senha: str
    pro_labore: float = 0.00

class UserInDB(UserCreate):
    idUsuario: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class UserResponse(BaseModel):
    idUsuario: int
    nome: str
    email: EmailStr
    celular: str
    pro_labore: float

    class Config:
        orm_mode = True

class UserDeleteResponse(BaseModel):
    message: str