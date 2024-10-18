from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.utils.listas_utils import lista_pertence_usuario
from app.models.embalagem import Embalagem

class EmbalagemRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, embalagem):
        try:
            self.db.add(embalagem)
            self.db.commit()
            self.db.refresh(embalagem)
            return embalagem
        except IntegrityError:
            self.db.rollback()
            return None
    
    def get_all(self, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return []
        return self.db.query(Embalagem).filter(Embalagem.idLista == lista_id).all()
    
    def get_by_id(self, embalagem_id: int, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return None
        return self.db.query(Embalagem).filter(
            Embalagem.idEmbalagens == embalagem_id,
            Embalagem.idLista == lista_id
        ).first()
    
    def update(self, embalagem_id: int, embalagem_data: Embalagem, lista_id: int, user_id: int):
        embalagem = self.get_by_id(embalagem_id, lista_id, user_id)
        if not embalagem:
            raise HTTPException(status_code=404, detail=f"Embalagem com ID {embalagem_id} não encontrado.")
        
        if embalagem_data.nome is not None:
            embalagem.nome = embalagem_data.nome
        if embalagem_data.unidade is not None:
            embalagem.unidade = embalagem_data.unidade
        if embalagem_data.preco_unidade is not None:
            embalagem.preco_unidade = embalagem_data.preco_unidade
        
        self.db.commit()
        self.db.refresh(embalagem)
        return embalagem
    
    def delete(self, embalagem_id: int, lista_id: int, user_id: int):
        embalagem = self.get_by_id(embalagem_id, lista_id, user_id)
        if embalagem:
            self.db.delete(embalagem)
            self.db.commit()
            return True
        else:
            return False
        
