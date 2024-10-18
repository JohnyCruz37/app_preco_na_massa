from pydantic import BaseModel
from typing import Optional

class EmbalagemCreate(BaseModel):
    nome: str
    unidade: int
    preco_unidade: float

class InsumoInDB(EmbalagemCreate):
    idEmbalagens: int
    idLista: int

    class Config:
        orm_mode = True

class EmbalagemUpdate(BaseModel):
    nome: Optional[str] = None
    unidade: Optional[int] = None
    preco_unidade: Optional[float] = None

    class Config:
        orm_mode = True

class EmbalagemResponse(BaseModel):
    idEmbalagens: int
    nome: str
    unidade: int
    preco_unidade: float
    idLista: int

    class Config:
        orm_mode = True

class EmbalagemDeleteResponse(BaseModel):
    message: str
