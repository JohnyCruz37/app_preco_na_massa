from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.dominio.value_objects.senha import Senha

class User(Base):
    __tablename__ = 'Usuario'
    idUsuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    celular = Column(String(20), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    pro_labore = Column(Float, nullable=False, default=0.00)

    listas = relationship('Listas', back_populates='usuario')

    def set_senha(self, senha:Senha):
        self.senha = senha.hash()

    def check_senha(self, senha:Senha) -> bool:
        return senha.verify(self.senha)
    
    def __repr__(self):
        return f'<User(nome="{self.nome}", email="{self.email}")>'