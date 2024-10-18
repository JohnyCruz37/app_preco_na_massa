from fastapi import APIRouter, HTTPException, Depends
from app.schemas.embalagem import EmbalagemCreate, EmbalagemDeleteResponse, EmbalagemUpdate, EmbalagemResponse
from app.dependencies import get_db_and_verify_token
from app.repository.embalagem import EmbalagemRepository
from app.repository.listas import ListasRepository
from app.services.embalagem import create_embalagem, get_all_embalagens, get_embalagem_by_id, update_embalagem, delete_embalagem

router = APIRouter()

@router.post("/{user_id}", response_model=EmbalagemResponse)
def create_embalagem_router(user_id, embalagem_data: EmbalagemCreate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = EmbalagemRepository(db)
    lista_repo = ListasRepository(db)

    if token_data["user_id"] != int(user_id):
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    return create_embalagem(embalagem_data, repo, lista_repo, token_data["user_id"])

@router.get("/{user_id}/{lista_id}", response_model=list[EmbalagemResponse])
def get_embalagens(user_id:int, lista_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = EmbalagemRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_all_embalagens(repo, lista_id, user_id)

@router.get("/{user_id}/{lista_id}/{embalagem_id}", response_model=EmbalagemResponse)
def get_embalagem_router(user_id:int, lista_id:int, embalagem_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = EmbalagemRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_embalagem_by_id(embalagem_id, repo, lista_id, user_id)

@router.put("/{user_id}/{lista_id}/{embalagem_id}", response_model=EmbalagemUpdate)
def update_embalagem_router(user_id:int, lista_id:int, embalagem_id:int, embalagem_data: EmbalagemUpdate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = EmbalagemRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    return update_embalagem(embalagem_id, embalagem_data, repo, lista_id, user_id)

@router.delete("/{user_id}/{lista_id}/{embalagem_id}", response_model=EmbalagemDeleteResponse)
def delete_embalagem_router(user_id:int, lista_id:int, embalagem_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = EmbalagemRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    delete_embalagem(embalagem_id, repo, lista_id, user_id)
    return {"message": "Insumo deletado com sucesso!"}