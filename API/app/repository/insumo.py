from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.utils.listas_utils import lista_pertence_usuario
from app.models.insumos import Insumo

class InsumoRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, insumo):
        try:
            self.db.add(insumo)
            self.db.commit()
            self.db.refresh(insumo)
            return insumo
        except IntegrityError:
            self.db.rollback()
            return None
    
    def get_all(self, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return []
        return self.db.query(Insumo).filter(Insumo.idLista == lista_id).all()
    
    def get_by_id(self, insumo_id: int, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return None
        return self.db.query(Insumo).filter(
            Insumo.idInsumos == insumo_id,
            Insumo.idLista == lista_id
        ).first()
    
    def update(self, insumo_id: int, insumo_data: Insumo, lista_id: int, user_id: int):
        insumo = self.get_by_id(insumo_id, lista_id, user_id)
        if not insumo:
            raise HTTPException(status_code=404, detail=f"Insumo com ID {insumo_id} não encontrado.")
        
        if insumo_data.nome is not None:
            insumo.nome = insumo_data.nome
        if insumo_data.unidade is not None:
            insumo.unidade = insumo_data.unidade
        if insumo_data.preco_unidade is not None:
            insumo.preco_unidade = insumo_data.preco_unidade
        
        self.db.commit()
        self.db.refresh(insumo)
        return insumo
    
    def delete(self, insumo_id: int, lista_id: int, user_id: int):
        insumo = self.get_by_id(insumo_id, lista_id, user_id)
        if insumo:
            self.db.delete(insumo)
            self.db.commit()
            return True
        else:
            return False