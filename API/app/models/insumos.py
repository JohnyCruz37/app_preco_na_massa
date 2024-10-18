from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Insumo(Base):
    __tablename__ = 'insumos'
    idInsumos = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    unidade = Column(Integer, nullable=False)
    preco_unidade = Column(Float, nullable=False)
    idLista = Column(Integer, ForeignKey('listas.idListas'), nullable=False)

    lista = relationship('Listas', back_populates='insumos')

    def __repr__(self):
        return f'<Insumo(nome="{self.nome}", unidade="{self.unidade}", preco_unidade="{self.preco_unidade}")>'
