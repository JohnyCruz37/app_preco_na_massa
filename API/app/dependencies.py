from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.utils.token_utils import verify_token

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_and_verify_token(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials 
    payload = verify_token(token)
    if "error" in payload:
        raise HTTPException(
            status_code=401,
            detail="Token Invalido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return db, payload
