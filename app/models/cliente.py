from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ ="Clientes"
    id = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    agendamentos = relationship("Agendamento", back_populates="cliente")