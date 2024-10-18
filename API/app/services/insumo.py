from fastapi import HTTPException
from app.schemas.insumo import InsumoCreate
from app.repository.insumo import InsumoRepository
from app.repository.listas import ListasRepository
from app.models.listas import Listas
from app.models.insumos import Insumo
def create_insumo(insumo_data: InsumoCreate, repo: InsumoRepository, lista_repo: ListasRepository, user_id: int):
    lista = lista_repo.get_by_id_user_and_tipo_lista("Insumos", user_id)
    if not lista:
        lista = Listas(
            tipo_lista = "Insumos",
            idUsuario = user_id
        )
        lista_repo.create(lista)

    insumo = Insumo(
        nome = insumo_data.nome,
        unidade = insumo_data.unidade,
        preco_unidade = insumo_data.preco_unidade,
        idLista = lista.idListas
    )
    try:
        return repo.create(insumo)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Insumo já cadastrado: {str(e)}")

def get_all_insumos(repo: InsumoRepository, lista_id: int, user_id: int):
    insumos = repo.get_all(lista_id, user_id)
    if not insumos:
        raise HTTPException(status_code=404, detail="Nenhum insumo encontrado.")
    return insumos

def get_insumo_by_id(insumo_id: int, repo: InsumoRepository, lista_id: int, user_id: int):
    insumo = repo.get_by_id(insumo_id, lista_id, user_id)
    if not insumo:
        raise HTTPException(status_code=404, detail=f"Insumo com ID {insumo_id} não encontrado.")
    return insumo

def update_insumo(insumo_id: int, insumo_data: InsumoCreate, repo: InsumoRepository, lista_id: int, user_id: int):
    existing_insumo = repo.get_by_id(insumo_id, lista_id, user_id)
    if not existing_insumo:
        raise HTTPException(status_code=404, detail=f"Insumo com ID {insumo_id} não encontrado.")
    try:
        return repo.update(insumo_id, insumo_data, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar insumo: {str(e)}")

def delete_insumo(insumo_id: int, repo: InsumoRepository, lista_id: int, user_id: int):
    insumo = repo.get_by_id(insumo_id, lista_id, user_id)
    if not insumo:
        raise HTTPException(status_code=404, detail=f"Insumo com ID {insumo_id} não encontrado.")
    try:
        repo.delete(insumo_id, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao deletar insumo: {str(e)}")