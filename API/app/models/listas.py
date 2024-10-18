from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Listas(Base):
    __tablename__ = 'listas'
    idListas = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo_lista = Column(String(12), nullable=False)
    idUsuario = Column(Integer, ForeignKey('Usuario.idUsuario'), nullable=False)

    usuario = relationship('User', back_populates='listas')
    ingredientes = relationship('Ingrediente', back_populates='lista')
    insumos = relationship('Insumo', back_populates='lista')
    embalagens = relationship('Embalagem', back_populates='lista')