from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.services.auth_service import authenticate_user
from app.dependencies import get_db
from app.utils.token_utils import create_access_token

router = APIRouter()

@router.post("/", response_model=dict ,tags=["login"])
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    access_token = create_access_token(data={"sub": authenticated_user.email, "user_id": authenticated_user.idUsuario})

    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }