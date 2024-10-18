import re

class Nome:
    def __init__(self, nome):
        if not self._validate_nome_e_sobrenome(nome):
            raise ValueError("Nome ou sobrenome inválido. Deve conter entre 3 e 50 caracteres.")
        self.nome = nome
    
    def _validate_nome_e_sobrenome(self, string_nome:str) -> bool:
        """
            Valida se o nome contém:
                1. Nome e sobrenome separados por um único espaço.
                3. Tanto o nome quanto o sobrenome devem ter pelo menos 3 caracteres.
        """
        nome_e_sobrenome = string_nome.split()
        if len(nome_e_sobrenome)!= 2:
            return False
        nome, sobrenome = nome_e_sobrenome
        return self._validate_string_nome(nome) and self._validate_string_nome(sobrenome)
    
    
    def _validate_string_nome(self, string:str) -> bool:
        """
            Valida se uma string (nome ou sobrenome):
                1. Tem entre 3 e 50 caracteres.
                2. Contém apenas letras e espaços.
        """
        if len(string) < 3 or len(string) > 50:
            return False
        if not re.match(r"^[a-zA-Z\s]+$", string):
            return False
        return True