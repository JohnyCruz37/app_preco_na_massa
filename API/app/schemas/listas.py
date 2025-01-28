from pydantic import BaseModel

class ListasCreate(BaseModel):
    tipo_lista: str
    idUsuario: int

class ListasInDB(ListasCreate):
    idListas: int

    class Config:
        from_attributes = True

