from fastapi import APIRouter, HTTPException, Depends
from app.schemas.insumo import InsumoCreate, InsumoUpdate, InsumoResponse, InsumoDeleteResponse
from app.dependencies import get_db_and_verify_token
from app.repository.insumo import InsumoRepository
from app.repository.listas import ListasRepository
from app.services.insumo import create_insumo, get_all_insumos, get_insumo_by_id, update_insumo, delete_insumo

router = APIRouter()

@router.post("/{user_id}", response_model=InsumoResponse)
def create_insumo_router(user_id, insumo_data: InsumoCreate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = InsumoRepository(db)
    lista_repo = ListasRepository(db)

    if token_data["user_id"] != int(user_id):
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    return create_insumo(insumo_data, repo, lista_repo, token_data["user_id"])

@router.get("/{user_id}/{lista_id}", response_model=list[InsumoResponse])
def get_insumos(user_id:int, lista_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = InsumoRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_all_insumos(repo, lista_id, user_id)

@router.get("/{user_id}/{lista_id}/{insumo_id}", response_model=InsumoResponse)
def get_insumo_router(user_id:int, lista_id:int, insumo_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = InsumoRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode verificar sua própria conta.")
    
    return get_insumo_by_id(insumo_id, repo, lista_id, user_id)

@router.put("/{user_id}/{lista_id}/{insumo_id}", response_model=InsumoUpdate)
def update_insumo_router(user_id:int, lista_id:int, insumo_id:int, insumo_data: InsumoUpdate, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = InsumoRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    return update_insumo(insumo_id, insumo_data, repo, lista_id, user_id)

@router.delete("/{user_id}/{lista_id}/{insumo_id}", response_model=InsumoDeleteResponse)
def delete_insumo_router(user_id:int, lista_id:int, insumo_id:int, db_and_token: tuple = Depends(get_db_and_verify_token)):
    db, token_data = db_and_token
    repo = InsumoRepository(db)
    if token_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Ação não permitida: você só pode realizar essa ação em sua própria conta.")
    
    delete_insumo(insumo_id, repo, lista_id, user_id)
    return {"message": "Insumo deletado com sucesso!"}