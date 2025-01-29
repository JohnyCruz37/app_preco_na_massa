from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
class UserRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def create(self, user):
        try:
            if self.get_by_email(user.email):
                raise HTTPException(status_code=409, detail="O email informado já está sendo utilizado.")
            
            if self.get_by_celular(user.celular):
                raise HTTPException(status_code=409, detail="O celular informado já está sendo utilizado.")


            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(status_code=409, detail=f"Erro de integridade ==> {e}")
    
    def delete(self, user_id: int):
        user = self.db.query(User).filter(User.idUsuario == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        else:
            raise ValueError("Usuário não encontrado")
    
    def get(self, user_id: int):
        user = self.db.query(User).filter(User.idUsuario == user_id).first()
        if user:
            return user
        else:
            raise ValueError("Usuário não encontrado")
    
    def get_by_email(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_celular(self, celular:str):
        return self.db.query(User).filter(User.celular == celular).first()
            
