import re

class Nome:
    EXCECOES = {"da", "de", "do", "das", "dos", "e"}
    def __init__(self, nome):
        if not self._validate_nome_e_sobrenome(nome):
            raise ValueError("Nome ou sobrenome inválido. Deve conter entre 3 e 50 caracteres.")
        self.nome = nome.strip()
    
    def _validate_nome_e_sobrenome(self, string_nome:str) -> bool:
        """
            Valida se o nome contém:
                1. Nome e sobrenome separados por um único espaço.
                3. Tanto o nome quanto o sobrenome devem ter pelo menos 3 caracteres.
        """
        nome_e_sobrenome = string_nome.strip().split()
        if len(nome_e_sobrenome) < 2:
            return False
        
        for i, parte in enumerate(nome_e_sobrenome):
            if parte.lower() in self.EXCECOES and i not in {0, len(nome_e_sobrenome)-1}:
                continue
            if not self._validate_string_nome(parte):
                return False
        
        return True
    
    def _validate_string_nome(self, string:str) -> bool:
        """
            Valida se uma string (nome ou sobrenome):
                1. Tem entre 3 e 50 caracteres.
                2. Contém apenas letras e espaços.
        """
        if not (3 <= len(string) <= 50):
            return False
        if not re.match(r"^[\wÀ-ÿ]+$", string, re.UNICODE):
            return False
        return True