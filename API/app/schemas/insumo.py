from pydantic import BaseModel
from typing import Optional

class InsumoCreate(BaseModel):
    nome: str
    unidade: int
    preco_unidade: float

class InsumoInDB(InsumoCreate):
    idInsumos: int
    idLista: int

    class Config:
        orm_mode = True

class InsumoUpdate(BaseModel):
    nome: Optional[str] = None
    unidade: Optional[int] = None
    preco_unidade: Optional[float] = None

    class Config:
        orm_mode = True

class InsumoResponse(BaseModel):
    idInsumos: int
    nome: str
    unidade: int
    preco_unidade: float
    idLista: int

    class Config:
        orm_mode = True

class InsumoDeleteResponse(BaseModel):
    message: str
