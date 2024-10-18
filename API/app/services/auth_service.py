from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserLogin
from bcrypt import  checkpw

def authenticate_user(db: Session, user_data: UserLogin):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        return None

    if not checkpw(user_data.senha.encode('utf-8'), user.senha.encode('utf-8')):
        return None

    return user
