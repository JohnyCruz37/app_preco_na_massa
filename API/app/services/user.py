from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.models.user import User
from app.repository.user import UserRepository
from app.dominio.value_objects.senha import Senha
from app.dominio.value_objects.nome import Nome

def create_user(user_data: UserCreate, repo: UserRepository):  
    senha_vo = Senha(user_data.senha) 
    nome_vo = Nome(user_data.nome)     
    user = User(
        nome = nome_vo.nome,
        email=user_data.email,
        celular=user_data.celular,
    )
    user.set_senha(senha_vo)
    try:
        return repo.create(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")

def delete_user(user_id: int, repo: UserRepository):
    try:
        return repo.delete(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuário: {str(e)}")

def get_user(user_id: int, repo: UserRepository):
    try:
        return repo.get(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar usuário: {str(e)}")