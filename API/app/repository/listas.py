from sqlalchemy.orm import Session
from app.models.listas import Listas

class ListasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, lista: Listas):
        self.db.add(lista)
        self.db.commit()
        self.db.refresh(lista)
        return lista
    
    def get_by_id_user(self, user_id: int):
        return self.db.query(Listas).filter(Listas.idUsuario == user_id).all()
    
    def get_by_id_user_and_tipo_lista(self, tipo_lista: str, user_id: int):
        return self.db.query(Listas).filter(Listas.idUsuario == user_id, Listas.tipo_lista == tipo_lista).first()