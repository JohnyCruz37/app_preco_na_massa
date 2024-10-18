import re
from passlib.context import CryptContext
from typing import Any

senha_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Senha:
    def __init__(self, senha: str):
        if not self._validate_senha(senha):
            raise ValueError("Senha inválida. Deve conter entre 8 e 20 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.")
        self.senha = senha
    
    @staticmethod
    def _validate_senha(senha: str) -> bool:
        if len(senha) < 8 or len(senha) > 20:
            return False
        if not re.search(r"[a-z]", senha):
            return False
        if not re.search(r"[A-Z]", senha):
            return False
        if not re.search(r"\d", senha):
            return False
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", senha):
            return False
        return True
    
    def hash(self) -> str:
        return senha_context.hash(self.senha)
    
    def verify(self, senha_hash: str) -> bool:
        return senha_context.verify(self.senha, senha_hash)
        