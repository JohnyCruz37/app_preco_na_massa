from pydantic import BaseModel, Field
from typing import Optional

class IngredienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    quantidade_compra: int = Field(..., gt=0, description="Quantidade comprada, deve ser maior que zero.")
    preco_compra: float = Field(..., gt=0, description="Preço de compra do ingrediente, deve ser maior que zero.")
    unidade_medida: str = Field(..., min_length=1, max_length=10, description="Unidade de medida do ingrediente.")
    quantidade_unidade_medida: int = Field(..., gt=0, description="Quantidade do ingrediente em unidade de medida.")

class IngredienteInDB(IngredienteCreate):
    idIngredientes: int
    idLista: int

    class Config:
        orm_mode = True

class IngredienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, max_length=50)
    quantidade_compra: Optional[int] = None
    preco_compra: Optional[float] = None
    unidade_medida: Optional[str] = Field(None, min_length=1)
    quantidade_unidade_medida: Optional[int] = None

    class Config:
        orm_mode = True

class IngredienteResponse(BaseModel):
    idIngredientes: int
    nome: str
    quantidade_compra: int
    preco_compra: float
    unidade_medida: str
    quantidade_unidade_medida: int
    idLista: int

    class Config:
        orm_mode = True

class IngredienteDeleteResponse(BaseModel):
    message: str