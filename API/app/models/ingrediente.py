from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    idIngredientes = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    quantidade_compra = Column(Integer, nullable=False)
    preco_compra = Column(Float, nullable=False)
    unidade_medida = Column(String(5), nullable=False)
    quantidade_unidade_medida = Column(Float, nullable=False)
    idLista = Column(Integer, ForeignKey('listas.idListas'), nullable=False)

    lista = relationship('Listas', back_populates='ingredientes')

    def __repr__(self):
        return f'<Ingrediente(nome="{self.nome}", quantidade_compra="{self.quantidade_compra}")>'