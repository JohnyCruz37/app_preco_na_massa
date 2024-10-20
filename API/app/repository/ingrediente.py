from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.ingrediente import Ingrediente
from app.models.listas import Listas
from app.utils.listas_utils import lista_pertence_usuario
from app.schemas.ingrediente import IngredienteUpdate

class IngredienteRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, ingrediente):
        try:
            self.db.add(ingrediente)
            self.db.commit()
            self.db.refresh(ingrediente)
            return ingrediente
        except IntegrityError:
            self.db.rollback()
            return None
    
    def get_all(self, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return []
        return self.db.query(Ingrediente).filter(Ingrediente.idLista == lista_id).all()
    
    def get_by_id(self, ingrediente_id: int, lista_id: int, user_id: int):
        if not lista_pertence_usuario(self.db, user_id, lista_id):
            return None
        return self.db.query(Ingrediente).filter(
            Ingrediente.idIngredientes == ingrediente_id,
            Ingrediente.idLista == lista_id
        ).first()

    def update(self, ingrediente_id:int, ingrediente_data: IngredienteUpdate, lista_id: int, user_id: int):
        ingrediente = self.get_by_id(ingrediente_id, lista_id, user_id)
        if not ingrediente:
            raise HTTPException(status_code=404, detail=f"Ingrediente com ID {ingrediente_id} não encontrado.")

        if ingrediente_data.nome is not None:
            ingrediente.nome = ingrediente_data.nome
        if ingrediente_data.quantidade_compra is not None:
            ingrediente.quantidade_compra = ingrediente_data.quantidade_compra
        if ingrediente_data.preco_compra is not None:
            ingrediente.preco_compra = ingrediente_data.preco_compra
        if ingrediente_data.unidade_medida is not None:
            ingrediente.unidade_medida = ingrediente_data.unidade_medida
        if quantidade_unidade_medida is not None:
            ingrediente.quantidade_unidade_medida = quantidade_unidade_medida

        self.db.commit()
        self.db.refresh(ingrediente)

        return ingrediente

    def delete(self, ingrediente_id: int, lista_id: int, user_id: int):
        ingrediente = self.get_by_id(ingrediente_id, lista_id, user_id)
        if ingrediente:
            self.db.delete(ingrediente)
            self.db.commit()
            return True
        else:
            return False