from sqlalchemy.orm import Session
from app.models.listas import Listas


def lista_pertence_usuario(db: Session, user_id: int, lista_id: int) -> bool:
    lista = db.query(Listas).filter(Listas.idListas == lista_id, Listas.idUsuario == user_id).first()
    return bool(lista)