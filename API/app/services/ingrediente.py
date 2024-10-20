from fastapi import HTTPException
from app.schemas.ingrediente import IngredienteCreate, IngredienteUpdate
from app.repository.ingrediente import IngredienteRepository
from app.repository.listas import ListasRepository
from app.models.ingrediente import Ingrediente
from app.models.listas import Listas

def create_ingrediente(ingrediente_data: IngredienteCreate, repo: IngredienteRepository, lista_repo: ListasRepository, user_id: int):
    lista = lista_repo.get_by_id_user_and_tipo_lista("Ingredientes", user_id)
    if not lista:
        lista = Listas(
            tipo_lista = "Ingredientes",
            idUsuario = user_id
        )
        lista = lista_repo.create(lista)

    ingrediente = Ingrediente(
        nome = ingrediente_data.nome,
        quantidade_compra = ingrediente_data.quantidade_compra,
        preco_compra = ingrediente_data.preco_compra,
        unidade_medida = ingrediente_data.unidade_medida,
        quantidade_unidade_medida = ingrediente_data.quantidade_unidade_medida,
        idLista = lista.idListas
    )
    try:
        return repo.create(ingrediente)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Ingrediente já cadastrado: {str(e)}")

def get_all_ingredientes(repo: IngredienteRepository, lista_id: int, user_id: int):
    ingredientes = repo.get_all(lista_id, user_id)
    if not ingredientes:
        raise HTTPException(status_code=404, detail="Nenhum ingrediente encontrado.")
    return ingredientes

def get_ingrediente_by_id(ingrediente_id: int, repo: IngredienteRepository, lista_id: int, user_id: int):
    ingrediente = repo.get_by_id(ingrediente_id, lista_id, user_id)
    if not ingrediente:
        raise HTTPException(status_code=404, detail=f"Ingrediente com ID {ingrediente_id} não encontrado.")
    return ingrediente

def update_ingrediente(ingrediente_id: int, ingrediente_data: IngredienteUpdate, repo: IngredienteRepository, lista_id: int, user_id: int):
    existing_ingrediente = repo.get_by_id(ingrediente_id, lista_id, user_id)
    if not existing_ingrediente:
        raise HTTPException(status_code=404, detail=f"Ingrediente com ID {ingrediente_id} não encontrado.")
    try:
        return repo.update(ingrediente_id, ingrediente_data, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar ingrediente: {str(e)}")

def delete_ingrediente(ingrediente_id: int, repo: IngredienteRepository, lista_id: int, user_id: int):
    ingrediente = repo.get_by_id(ingrediente_id, lista_id, user_id)
    if not ingrediente:
        raise HTTPException(status_code=404, detail=f"Ingrediente com ID {ingrediente_id} não encontrado.")

    try:
        return repo.delete(ingrediente_id, lista_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao deletar ingrediente: {str(e)}")