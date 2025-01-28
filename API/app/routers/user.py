from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserDeleteResponse
from app.services.user import create_user, delete_user
from app.dependencies import get_db, get_db_and_verify_token
from app.repository.user import UserRepository

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def register_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    body = await request.body()
    print(f"Request: {body}")
    try:
        user_repository = UserRepository(db)
        db_user = create_user(user, user_repository)
        return db_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")
    
@router.delete("/{user_id}", response_model=UserDeleteResponse)
def delete_user_route(user_id: int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = UserRepository(db)

    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode deletar sua própria conta.")
    
    try:
        delete_user(user_id, repo)
        return {"message": "Usuário excluído com sucesso"}
    except HTTPException as e:
        raise e

@router.get("/{user_id}", response_model=UserResponse)
def get_user_route(user_id: int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = UserRepository(db)

    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    try:
        user = repo.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return user
    except HTTPException as e:
        raise e