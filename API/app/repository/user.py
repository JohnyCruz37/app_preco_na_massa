from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
class UserRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def create(self, user):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise ValueError(status_code=409, detail="Usuário já cadastrado")
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Erro ao criar usuário: {str(e)}")
    
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