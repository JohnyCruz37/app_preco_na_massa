from fastapi import HTTPException
from app.schemas.embalagem import EmbalagemCreate
from app.repository.embalagem import EmbalagemRepository
from app.repository.listas import ListasRepository
from app.models.listas import Listas
from app.models.embalagem import Embalagem
def create_embalagem(embalagem_data: EmbalagemCreate, repo: EmbalagemRepository, lista_repo: ListasRepository, user_id: int):
    lista = lista_repo.get_by_id_user_and_tipo_lista("Embalagens", user_id)
    if not lista:
        lista = Listas(
            tipo_lista = "Embalagens",
            idUsuario = user_id
        )
        lista_repo.create(lista)

    embalagem = Embalagem(
        nome = embalagem_data.nome,
        unidade = embalagem_data.unidade,
        preco_unidade = embalagem_data.preco_unidade,
        idLista = lista.idListas
    )
    try:
        return repo.create(embalagem)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Embalagem já cadastrado: {str(e)}")

def get_all_embalagens(repo: EmbalagemRepository, lista_id: int, user_id: int):
    embalagem = repo.get_all(lista_id, user_id)
    if not embalagem:
        raise HTTPException(status_code=404, detail="Nenhuma embalagem encontrado.")
    return embalagem

def get_embalagem_by_id(embalagem_id: int, repo: EmbalagemRepository, lista_id: int, user_id: int):
    embalagem = repo.get_by_id(embalagem_id, lista_id, user_id)
    if not embalagem:
        raise HTTPException(status_code=404, detail=f"Embalagem com ID {embalagem_id} não encontrado.")
    return embalagem

def update_embalagem(embalagem_id: int, embalagem_data: EmbalagemCreate, repo: EmbalagemRepository, lista_id: int, user_id: int):
    existing_embalagem = repo.get_by_id(embalagem_id, lista_id, user_id)
    if not existing_embalagem:
        raise HTTPException(status_code=404, detail=f"Insumo com ID {embalagem_id} não encontrado.")
    try:
        return repo.update(embalagem_id, embalagem_data, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar embalagem: {str(e)}")

def delete_embalagem(embalagem_id: int, repo: EmbalagemRepository, lista_id: int, user_id: int):
    embalagem = repo.get_by_id(embalagem_id, lista_id, user_id)
    if not embalagem:
        raise HTTPException(status_code=404, detail=f"Embalagem com ID {embalagem_id} não encontrado.")
    try:
        repo.delete(embalagem_id, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao deletar embalagem: {str(e)}")