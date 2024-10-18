from fastapi import APIRouter, HTTPException, Depends

from app.schemas.ingrediente import IngredienteCreate, IngredienteResponse, IngredienteUpdate, IngredienteDeleteResponse
from app.dependencies import get_db_and_verify_token
from app.services.ingrediente import create_ingrediente, get_all_ingredientes, get_ingrediente_by_id, update_ingrediente, delete_ingrediente
from app.repository.ingrediente import IngredienteRepository
from app.repository.listas import ListasRepository

router = APIRouter()

@router.post("/{user_id}", response_model=IngredienteResponse)
def create_ingrediente_router(user_id, ingrediente_data: IngredienteCreate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = IngredienteRepository(db)
    lista_repo = ListasRepository(db)

    if token_data["user_id"] != int(user_id):
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")

    return create_ingrediente(ingrediente_data, repo, lista_repo, token_data["user_id"])

@router.get("/{user_id}/{lista_id}", response_model=list[IngredienteResponse])
def get_ingredientes(user_id:int, lista_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = IngredienteRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_all_ingredientes(repo, lista_id, user_id)

@router.get("/{user_id}/{lista_id}/{ingrediente_id}", response_model=IngredienteResponse)
def get_ingrediente(user_id:int, lista_id:int, ingrediente_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = IngredienteRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_ingrediente_by_id(ingrediente_id, repo, lista_id, user_id)

@router.put("/{user_id}/{lista_id}/{ingrediente_id}", response_model=IngredienteUpdate)
def update_ingrediente_route(user_id:int, lista_id:int, ingrediente_id:int, ingrediente_data: IngredienteUpdate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = IngredienteRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    return update_ingrediente(ingrediente_id, ingrediente_data, repo, lista_id, user_id)

@router.delete("/{user_id}/{lista_id}/{ingrediente_id}", response_model=IngredienteDeleteResponse)
def delete_ingrediente_route(user_id:int,lista_id:int, ingrediente_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = IngredienteRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    delete_ingrediente(ingrediente_id, repo, lista_id, user_id)
    return {"message": "Ingrediente deletado com sucesso!"}